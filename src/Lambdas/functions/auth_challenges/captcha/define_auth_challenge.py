def lambda_handler(event, context):
    # Always enforce CAPTCHA, even if password is correct
    event['response'] = {
        'challengeName': 'CUSTOM_CHALLENGE',  # Your challenge name
        'issueTokens': False,  # Don't issue tokens yet
        'failAuthentication': False  # Don't fail, just challenge
    }
    return event