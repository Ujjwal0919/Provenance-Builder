from prov.model import ProvDocument
from prov.dot import prov_to_dot
import utilities

default_prov_image = "default_provenance.png"
user_prov_image = "user_provenance.png"
policy_prov_image = "policy_provenance.png"
policy_1 = {"name": "policy_1", "allowed_ports": 50}
policy_2 = {"name": "policy_2", "allowed_ports": 4535}
Access_Control = 0
Policy_Control = 0

# Create a list of policies
policies = [policy_1, policy_2]


def generate_default_provenance():
    # Create a new provenance document
    doc = ProvDocument()

    # Add namespaces
    doc.add_namespace("ex", "http://example.com/")

    # Define agents
    sensor = doc.agent("ex:sensor")
    controller = doc.agent("ex:controller")
    robotic_arm = doc.agent("ex:robotic_arm")

    # Define activities
    temperature_publish = doc.activity("ex:temperature_publish")
    temperature_subscribe = doc.activity("ex:temperature_subscribe")
    alert_publish = doc.activity("ex:alert_publish")
    alert_subscribe = doc.activity("ex:alert_subscribe")

    # Define entities
    temperature = doc.entity("ex:temperature")
    subscribed_temperature = doc.entity("ex:subscribed_temperature")
    alert = doc.entity("ex:alert")
    subscribed_alert = doc.entity("ex:subscribed_alert")

    # Define relationships
    doc.wasAttributedTo(temperature, sensor)
    doc.wasAssociatedWith(temperature_publish, sensor)
    doc.wasGeneratedBy(temperature, temperature_publish)

    doc.wasAttributedTo(subscribed_temperature, controller)
    doc.wasAssociatedWith(temperature_subscribe, controller)
    doc.wasGeneratedBy(subscribed_temperature, temperature_subscribe)

    doc.wasAttributedTo(alert, controller)
    doc.wasAssociatedWith(alert_publish, controller)
    doc.wasGeneratedBy(alert, alert_publish)

    doc.wasAttributedTo(subscribed_alert, robotic_arm)
    doc.wasAssociatedWith(alert_subscribe, robotic_arm)
    doc.wasGeneratedBy(subscribed_alert, alert_subscribe)
    return doc


def generate_graph(document, name):
    dot = prov_to_dot(document)
    dot.write_png(name)


def generate_provenance_logs(logs):
    # Create a new provenance document
    doc_log = ProvDocument()
    # Define namespaces
    ex = doc_log.add_namespace("ex", "http://example.com/")
    entities = {}
    activities = {}
    agents = {}

    for log in logs:
        # Create agents
        if log["agent"] not in agents:
            agent = doc_log.agent(ex[log["agent"]])
            agents[log["agent"]] = agent
        # Create activities
        if log["activity"] not in activities:
            activity = doc_log.activity(ex[log["activity"]])
            activities[log["activity"]] = activity
        # Create entities
        if log["entity"] not in entities:
            entity = doc_log.entity(ex[log["entity"]])
            entities[log["entity"]] = entity
        # Add relationships
        if "relationships" in log:
            for relationship in log["relationships"]:
                rel_type = relationship["type"]
                if rel_type == "wasAttributedTo":
                    doc_log.wasAttributedTo(entity, agent)
                elif rel_type == "wasAssociatedWith":
                    agent_rel = relationship.get("agent")
                    if agent_rel:
                        doc_log.wasAssociatedWith(activity, agents[agent_rel])
                elif rel_type == "wasGeneratedBy":
                    activity_rel = relationship.get("activity")
                    if activity_rel:
                        doc_log.wasGeneratedBy(entity, activities[activity_rel])

    generate_graph(doc_log, user_prov_image)
    return doc_log


def is_malicious(provobj, provobj1, a):
    if a == 1:
        if provobj == provobj1:
            utilities.print_success("Logs are not malicious")
            utilities.display_images_with_captions(default_prov_image, user_prov_image, "Default Provenance",
                                                   "Logs Provenance")
        else:
            utilities.print_alert("Logs are malicious")
            utilities.display_images_with_captions(default_prov_image, user_prov_image, "Default Provenance",
                                                   "Logs Provenance")
    if a == 2:
        utilities.display_images_with_captions(default_prov_image, policy_prov_image, "Default Provenance",
                                               "Logs Provenance")


def create_policy():
    policy_name = input("Enter the name of Policy: ")
    allowed_port = input("Enter the port number that you want to wishlist: ")
    new_policy = {"name": policy_name, "allowed_port": allowed_port}
    policies.append(dict(new_policy))
    print("*************** NEW POLICY ADDED ***************")
    print(policies)


def check_policy(entity_port):
    for policy in policies:
        if entity_port in policy["allowed_ports"]:
            return policy["name"]
    return "No Policy Matched"


def policy_provenance(logs):
    global Access_Control
    global Policy_Control
    print(policies)
    if len(policies) == 0:
        print("No Policies Found!!! Implement Policies First")
    else:
        doc_log = ProvDocument()
        ex = doc_log.add_namespace("ex", "http://example.com/")
        entities = {}
        activities = {}
        agents = {}
        for log in logs:
            # Create agents
            if log["agent"] not in agents:
                agent = doc_log.agent(ex[log["agent"]])
                agents[log["agent"]] = agent

            # Create activities
            if log["activity"] not in activities:
                activity = doc_log.activity(ex[log["activity"]])
                activities[log["activity"]] = activity

            # Create entities
            if log["entity"] not in entities:
                entity = doc_log.entity(ex[log["entity"]])
                entities[log["entity"]] = entity

            # Add relationships
            if "relationships" in log:
                for relationship in log["relationships"]:
                    rel_type = relationship["type"]
                    if rel_type == "wasAttributedTo":
                        doc_log.wasAttributedTo(entity, agent)
                    elif rel_type == "wasAssociatedWith":
                        agent_rel = relationship.get("agent")
                        if agent_rel:
                            doc_log.wasAssociatedWith(activity, agents[agent_rel])
                    elif rel_type == "wasGeneratedBy":
                        activity_rel = relationship.get("activity")
                        if activity_rel:
                            doc_log.wasGeneratedBy(entity, activities[activity_rel])
        default_prov = generate_default_provenance()
        if doc_log == default_prov:
            Access_Control = 1
        print("Access Control Done")
        for log in logs:
            agent_name = log["agent"]
            port = log["data"].get("port")
            for policy in policies:
                if port == policy["allowed_ports"]:
                    Policy_Control = 1
                    utilities.print_success("Policy Name: " + policy["name"] + " applied at agent: " + agent_name)
                    if agent_name in agents:
                        agent = agents[agent_name]
                        doc_log.wasAttributedTo(agent, ex["Policy_Implemented"])
                else:
                    Policy_Control = 0
                    utilities.print_alert("Policy Name: " + policy["name"] + " violated at agent: " + agent_name)
        print(Access_Control)
        print(Policy_Control)
        if Access_Control == 1 and Policy_Control == 1:
            utilities.print_success("Logs are not malicious")
        else:
            utilities.print_alert("Logs are malicious")

        generate_graph(doc_log, policy_prov_image)
        return doc_log
