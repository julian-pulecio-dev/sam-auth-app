import random

def lambda_handler(event, context):
    # Must match DefineAuthChallenge's name exactly
    CHALLENGE_NAME = "CUSTOM_SRP_CHALLENGE"  
    
    if event['triggerSource'] == "CreateAuthChallenge_Authentication":
        # Generate a 6-digit OTP (example challenge)
        otp_code = str(random.randint(100000, 999999))
        
        event['response'] = {
            'publicChallengeParameters': {
                'hint': 'Enter the 6-digit code',
                'codeLength': '6'
            },
            'privateChallengeParameters': {
                'answer': otp_code  # Secret correct answer
            },
            'challengeMetadata': CHALLENGE_NAME  # Must match!
        }
        
        # In production, send OTP via email/SMS here
        print(f"DEBUG: Generated OTP {otp_code} for {event['userName']}")
    
    return event