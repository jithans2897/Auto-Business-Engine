from app.models.project import Project
from app.models.resource import Resource


def react_agent_loop(db, project_id):

    thoughts = []
    actions = []
    observations = []

    # STEP 1: THINK
    project = db.query(Project).filter(Project.id == project_id).first()
    resources = db.query(Resource).filter(Resource.project_id == project_id).all()

    total_cost = sum(r.cost_per_month for r in resources)

    thought = f"Project cost is {total_cost}"
    thoughts.append(thought)

    # STEP 2: DECIDE
    if total_cost > 1000:
        decision = "Cost too high, reduce resources"
    else:
        decision = "Cost is under control"

    thoughts.append(decision)

    # STEP 3: ACT
    if total_cost > 1000:
        for r in resources:
            if r.cost_per_month > 300:
                r.cost_per_month *= 0.9
                action = f"Reduced cost of {r.name}"
                actions.append(action)

    db.commit()

    # STEP 4: OBSERVE
    updated_resources = db.query(Resource).filter(Resource.project_id == project_id).all()
    new_cost = sum(r.cost_per_month for r in updated_resources)

    observation = f"New total cost is {new_cost}"
    observations.append(observation)

    return {
        "thoughts": thoughts,
        "actions": actions,
        "observations": observations
    }