# app/api/workflow.py
from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..extensions import db
from ..models import Workflow, WorkflowStep
from ..tasks.ai_tasks import analyze_proposal_task

ns = Namespace('workflows', description='Workflow operations')

payload_model = ns.model('Payload', {
    'text': fields.String(required=True)
})

workflow_model = ns.model('Workflow', {
    'name': fields.String(required=True),
    'payload': fields.Nested(payload_model)
})

@ns.route('')
class WorkflowCreate(Resource):
    @ns.expect(workflow_model)
    @jwt_required()
    def post(self):
        data = ns.payload
        user_id = get_jwt_identity()

        workflow = Workflow(name=data['name'], user_id=user_id)
        db.session.add(workflow)
        db.session.commit()

        # Dispara análise de IA assíncrona
        if data['name'] == 'proposal_approval':
            analyze_proposal_task.delay(workflow.id, data['payload']['text'])

        return {"workflow_id": workflow.id, "status": "started"}, 202