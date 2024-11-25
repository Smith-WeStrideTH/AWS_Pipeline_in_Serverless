
def lambda_handler(event, context):
    try :
        for record in event['Records']:
            if record['eventName'] == 'INSERT':
                handle_insert(record)
            elif record['eventName'] == 'MODIFY':
                handle_modify(record)
            elif record['eventName'] == 'REMOVE':
                handle_reomove(record)

    except Exception as e:
        print(e)

def handle_insert(record):
    print("Handling INSERT event")
    #get image
    new_image = record['dynamodb']['NewImage']
    #parse value
    new_playerId = new_image['playerId']['S']
    print(f'New row added with playerId = {new_playerId}')
    print("Done Handling INSERT")

def handle_modify(record):
    print("Handling MODIFY event")
    old_image = record['dynamodb']['OldImage']
    old_score = old_image['score']['N']

    new_image = record['dynamodb']['NewImage']
    new_score = new_image['score']['N']

    # old_score += new_score
    if  old_score != new_score:
        print(f'Score Changed : {old_score} (Old Score) {new_score} (New Score)')
    print("Done Handling Modify")

def handle_reomove(record):
    print("Handling REMOVE event")
    old_image = record['dynamodb']['OldImage']
    old_playerId = old_image['playerId']['S']
    print(f'Removed playerId = {old_playerId}')
    print("Done Handling Remove")








