def lambda_handler(event, context):
    """
    Define the next step in the custom auth flow.
    """
    print("DefineAuthChallenge event:", event)

    # If the user is already authenticated
    if event['session'] and event['session'][-1]['challengeResult']:
        event['response']['issueTokens'] = True
        event['response']['failAuthentication'] = False
    # If the number of challenges exceeds a limit (e.g., 3 attempts)
    elif len(event['session']) >= 3:
        event['response']['issueTokens'] = False
        event['response']['failAuthentication'] = True
    # Otherwise, keep challenging the user
    else:
        event['response']['issueTokens'] = False
        event['response']['failAuthentication'] = False
        event['response']['challengeName'] = 'CUSTOM_CHALLENGE'

    return event