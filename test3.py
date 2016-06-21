import phantom.rules as phantom
import json

def geolocate_ip_1(container, action=None, success=None, results=None, handle=None, filtered_ids=None):
    
    
    parameters = []
    
    parameters.append({
        'ip': "1.1.1.1",
    })


    phantom.act("geolocate ip", parameters=parameters, assets=['maxmind'], name="geolocate_ip_1")    

    return


def on_start(container):
    geolocate_ip_1(container)

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