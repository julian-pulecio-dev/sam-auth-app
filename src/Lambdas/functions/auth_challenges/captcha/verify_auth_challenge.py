def lambda_handler(event, context):
    """
    Verify the user's response to the custom challenge (e.g., check the OTP).
    """
    print("VerifyAuthChallengeResponse event:", event)

    # Extract the expected answer and the user's response
    expected_answer = event['request']['privateChallengeParameters'].get('answer')
    user_answer = event['request']['challengeAnswer']

    print(f"Expected: {expected_answer}, User provided: {user_answer}")

    # Check if the user answered correctly
    if user_answer == expected_answer:
        event['response']['answerCorrect'] = True
    else:
        event['response']['answerCorrect'] = False

    return event
