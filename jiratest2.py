import phantom.rules as phantom
import json
from datetime import datetime, timedelta

def on_start(container):
    
    # call 'list_projects' block
    list_projects(container)

    return

def list_projects(container, filtered_artifacts=None, filtered_results=None):

    parameters = []

    phantom.act("list projects", parameters=parameters, assets=['jira'], callback=decision_1, name="list_projects")
    
    return

def list_tickets(action, success, container, results, handle, filtered_artifacts=None, filtered_results=None):
    
    #phantom.debug('Action: {0} {1}'.format(action['action_name'], ('SUCCEEDED' if success else 'FAILED')))
    
    filter_results_data_1 = phantom.collect2(container=container, action_results=filtered_results, datapath=["action_result.data.*.project_key"])

    parameters = []
    
    for filter_results_item_1 in filter_results_data_1:
        parameters.append({
            'query': "",
            'max_results': "",
            'project_key': filter_results_item_1[0],
            'start_index': "",
        })

    phantom.debug('ticket list: {}'.format(parameters))
    if parameters:
        phantom.act("list tickets", parameters=parameters, assets=['jira'], name="list_tickets")    
    
    return

def decision_1(action, success, container, results, handle, filtered_artifacts=None, filtered_results=None):

    # collect filtered artifact ids for 'if' condition 1
    matched_artifacts_1, matched_results_1 = phantom.condition(
        container=container,
        action_results=results,
        conditions=[
            ["list_projects:action_result.data.*.project_key", "==", "AP"],
        ])

    # call connected blocks if filtered artifacts or results
    if matched_artifacts_1 or matched_results_1:
        list_tickets(action, success, container, results, handle, filtered_artifacts=matched_artifacts_1, filtered_results=matched_results_1)

    return

def on_finish(container, summary):

    # This function is called after all actions are completed.
    # Summary and/or action results can be collected here.

    # summary_json = phantom.get_summary()
    # summary_results = summary_json['result']
    # for result in summary_results:
            # action_run_id = result['id']
            # action_results = phantom.get_action_results(action_run_id=action_run_id)

    return
