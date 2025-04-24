def lambda_handler(event, context):
    # Your custom challenge name - define once here
    CHALLENGE_NAME = "CUSTOM_SRP_CHALLENGE"  # ⭐ Change this to your preferred name
    
    if event['triggerSource'] == "DefineAuthChallenge_Authentication":
        sessions = event['request']['session']
        
        # Case 1: Fresh auth after SRP - initiate custom challenge
        if not sessions:
            event['response'] = {
                'challengeName': CHALLENGE_NAME,
                'issueTokens': False,
                'failAuthentication': False
            }
        
        # Case 2: User completed challenge - validate
        elif sessions[-1]['challengeName'] == CHALLENGE_NAME:
            if sessions[-1]['challengeResult']:  # Challenge passed
                event['response']['issueTokens'] = True
            else:  # Challenge failed
                event['response']['failAuthentication'] = True
                
    return event