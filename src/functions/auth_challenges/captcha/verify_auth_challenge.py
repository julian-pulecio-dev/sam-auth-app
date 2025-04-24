def lambda_handler(event, context):
    if event['triggerSource'] == "VerifyAuthChallengeResponse_Authentication":
        # Get stored correct answer
        private_answer = event['request']['privateChallengeParameters']['answer']
        # Get user's attempt
        user_answer = event['request']['challengeAnswer']
        
        event['response']['answerCorrect'] = (user_answer == private_answer)
        
        print(f"DEBUG: Expected {private_answer}, got {user_answer}")
    
    return event