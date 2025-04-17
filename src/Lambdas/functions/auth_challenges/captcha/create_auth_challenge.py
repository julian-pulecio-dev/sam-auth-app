import random

def lambda_handler(event, context):
    """
    Create a custom challenge for the user, e.g., generate and send a one-time code.
    """
    print("CreateAuthChallenge event:", event)

    # Only issue a new challenge if this is a new session or the last challenge failed
    if event['triggerSource'] == 'CreateAuthChallenge_Authentication' and (
        not event['session'] or not event['session'][-1]['challengeResult']
    ):
        # Generate a 6-digit code
        challenge_code = str(random.randint(100000, 999999))
        
        # Store the code in private challenge parameters (not sent to the client)
        event['response']['privateChallengeParameters'] = {
            'answer': challenge_code
        }

        # Return the challenge parameters (these go to the client)
        event['response']['publicChallengeParameters'] = {
            'challengeType': 'OTP'
        }

        # Include metadata that can be passed to the verify function
        event['response']['challengeMetadata'] = f"CODE-{challenge_code}"

        # Simulate sending the code - in production, use SNS, SES, etc.
        print(f"Sending OTP code to user: {challenge_code}")

    else:
        # Don't issue a new challenge if the previous one succeeded
        event['response']['publicChallengeParameters'] = {}
        event['response']['privateChallengeParameters'] = {}
        event['response']['challengeMetadata'] = ''

    return event
