@service
def example_service(action=None, id=None):
    """example using pyscript."""
    log.info(f"hello world: got action {action} id {id}")
    if action == "turn_on" and id is not None:
        light.turn_on(entity_id=id, brightness=255)
    elif action == "fire" and id is not None:
        event.fire(id, param1=12, pararm2=80)
