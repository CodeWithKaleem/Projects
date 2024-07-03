from flask import Flask,request

app = Flask(__name__)

# Create a idea repository 

ideas = {
    1 : {
        'id': 1,
        'idea_name':'kaleem',
        'idea_description': 'Python Developer'
    },
    2: {
        'id': 2,
        'idea_name':'shaheem',
        'idea_description':'Data analyst'
    }
}

'''
Create a Restful endpoint for fetching all the ideas
'''

@app.get("/IdeaApp/api/v1/ideas")
def get_all_idea():
    # I need to read the query param
    idea_name  = request.args.get("idea_name")
    if idea_name:
        idea_res = {}
        # Now i need to filter the ideas created by this author
        for key,value in ideas.items():
            if value['idea_name']== idea_name:
                idea_res[key]= value
        return idea_res
    return ideas

'''
Create a Restful enpoint for creating an new idea
'''
@app.post("/IdeaApp/api/v1/ideas")
def create_idea():
    # Login to create idea
    try :
        # first read the request body
        request_body = request.get_json()

        # check if passed idea is not present already
        if request_body["id"] and request_body["id"] in ideas:
            return 'idea with the same id is already present',400
        # Insert the passed idea into the ideas dictionary
        ideas[request_body["id"]] = request_body
        # Return the response saying idea saved successfully
        return 'Idea created and saved successfully',201
    except KeyError:
        return 'id is missing',400
    except:
        return "Some internal server error",500
    
'''
End point to fetch idea based on idea id
'''
@app.get("/IdeaApp/api/v1/ideas/<idea_id>")
def get_idea_id(idea_id):
    try:
        if int(idea_id) in ideas:
            return ideas[int(idea_id)],200
        else:
            return 'idea id is not present',400

    except:
        return "Some internal error occured",500
    
'''
Creating an endpoint for updating the idea
'''
@app.put("/IdeaApp/api/v1/ideas/<idea_id>")
def update_idea(idea_id):
    try:
        if int(idea_id) in ideas:
            ideas[int(idea_id)]= request.get_json()
            return ideas[int(idea_id)],200
        else:
            return 'idea id is not present',400

    except:
        return "Some internal error occured",500


'''
Creating an endpoint for deleting the idea
'''
@app.delete("/IdeaApp/api/v1/ideas/<idea_id>")
def delete_idea(idea_id):
    try:
        if int(idea_id) in ideas:
            del ideas[int(idea_id)]
            return f'Idea Id {int(idea_id)} is sucessfully deleted',200
    except:
        return 'Idea Id is not present',400


if __name__ == '__main__':
    app.run(port=8080)

