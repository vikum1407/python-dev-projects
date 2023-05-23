from Controllers.subjectController import crudSubject
from Controllers.studentController import crudStudent
from Controllers.resultController import crudResult

# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, request, jsonify
 
# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)
 
# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.

#===================== Student ======================================
@app.route('/api/v1/student/', methods=['POST'])
#Adding new Student
def add_student():
    request_data = request.get_json()

    studentID = request_data['studentID']
    studentName = request_data['studentName']

    crudStudent.add_student(crudStudent,studentID, studentName)

    return {'message': 'Student added successfully.'}


@app.route('/api/v1/student/<id>', methods=['GET'])
def get_student(id):

    result = crudStudent.get_student_value(crudStudent,int(id))

    if result != -1:
        # Assuming the result is the index of the matched student in the student_table
        #student = crudStudent.student_table[id]
        return jsonify({"id": result.getStudentID(), "name": result.getStudentName()})
    else:
        return jsonify({"error": "Student not found"}), 404
    

@app.route('/api/v1/student/<id>', methods=['PUT'])
def edit_student(id):
    request_data = request.get_json()

    studentName = request_data['studentName']

    result = crudStudent.edit_student(crudStudent, int(id), studentName)

    if result != -1:
        return {'message': 'Student edit successfully.'}
    else:
        return jsonify({"error": "Student not found"}), 404


@app.route('/api/v1/student/<id>', methods=['DELETE'])
def del_student(id):

    result = crudStudent.del_student(crudStudent,int(id))

    if result != -1:
        # Assuming the result is the index of the matched student in the student_table
        #student = crudStudent.student_table[id]
        return {'message': 'Student delete successfully.'}
    else:
        return jsonify({"error": "Student not found"}), 404


#============================ Subject ==========================================

@app.route('/api/v1/subject/', methods=['POST'])
#Adding new Subject
def add_subject():
    request_data = request.get_json()

    subjectID = request_data['subjectID']
    subjectName = request_data['subjectName']

    crudSubject.add_subject(crudSubject, subjectID, subjectName)

    return {'message': 'Subject added successfully.'}

@app.route('/api/v1/subject/<id>', methods=['GET'])
def get_subject(id):

    result = crudSubject.get_subject_value(crudSubject, int(id))

    if result != -1:
        # Assuming the result is the index of the matched subject in the subject_table
        return jsonify({"id": result.getSubjectID(), "name": result.getSubjectName()})
    else:
        return jsonify({"error": "Subject not found"}), 404
    
@app.route('/api/v1/subject/<id>', methods=['PUT'])
def edit_subject(id):
    request_data = request.get_json()

    subjectName = request_data['subjectName']

    result = crudSubject.edit_subject(crudSubject, int(id), subjectName)

    if result != -1:
        return {'message': 'Subject edit successfully.'}
    else:
        return jsonify({"error": "Subject not found"}), 404


@app.route('/api/v1/subject/<id>', methods=['DELETE'])
def del_subject(id):

    result = crudSubject.del_subject(crudSubject, int(id))

    if result != -1:
        # Assuming the result is the index of the matched student in the student_table
        return {'message': 'Subject delete successfully.'}
    else:
        return jsonify({"error": "Subject not found"}), 404
    

#============================ Result ==========================================

@app.route('/api/v1/result/', methods=['POST'])
#Adding new Result
def add_result():
    request_data = request.get_json()

    studentID = request_data['studentID']
    subjectID = request_data['subjectID']
    result = request_data['result']

    crudResult.add_result(crudResult, studentID, subjectID, result)

    return {'message': 'Result added successfully.'}


@app.route('/api/v1/result/<id>', methods=['GET'])
def get_result(id):

    result = crudResult.get_result_value(crudResult, int(id))

    if result != -1:
        # Assuming the result is the index of the matched subject in the subject_table
        return jsonify({"id": result.getSubject(), "mark": result.getMarks()})
    else:
        return jsonify({"error": "Student not found"}), 404


@app.route('/api/v1/result/<id>', methods=['PUT'])
def edit_result(id):
    request_data = request.get_json()

    subjectID = request_data['subjectID']
    mark = request_data['mark']

    result = crudResult.edit_result(crudResult, int(id), subjectID, mark)

    if result != -1:
        return {'message': 'Result edit successfully.'}
    else:
        return jsonify({"error": "Student not found"}), 404
    

@app.route('/api/v1/result/<id1>/<id2>', methods=['DELETE'])
def del_result(id1,id2):

    result = crudResult.del_result(crudResult, int(id1), int(id2))

    if result != -1:
        # Assuming the result is the index of the matched student in the student_table
        return {'message': 'Result delete successfully.'}
    else:
        return jsonify({"error": "Student not found"}), 404

 
# main driver funct

if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.
    app.run(debug=True)