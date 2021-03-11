@app.route("/pending/enrollments", methods=["GET"])
def pending_enrol():
    last_call = mongo.db.refactored.find({"Name": "pending"})[0]
    return {"status": True, "data": last_call["Count"]}, 200

@app.route("/all/enrollments", methods=["GET"])
def all_enroll():
    last_call = mongo.db.refactored.find({"Name": "all_enroll"})[0]
    return {"status": True, "data": last_call["Count"]}, 200


@app.route("/enrollment/verify", methods=["GET"])
def verify_ID():
    parser = reqparse.RequestParser(bundle_errors=True)
    parser.add_argument("ENRID", type=str, required=True, help="this field cannot be left blank")
    data = parser.parse_args()
    q_result = mongo.db.Approved.find_one({"ENRID": data["ENRID"]}, {"ENRID": 1, "Plan": 1, "Name": 1, "_id": 0})
    if q_result:  # len(v_result) > 0
        if q_result["Plan"] == "Informal":
            reference_num = str(uuid.uuid4().int)[:7] + str(date.today()).replace("-","")
            q_result["total_amount"] = "12000"
            q_result["reference_number"] = reference_num
            q_result["Date"] = str(datetime.now())
            mongo.db.ussd_subs.update({"ENRID": q_result["ENRID"]},{"$push": {"Subs": q_result}},upsert=True)
            del q_result["Date"]
            return {"status": True, "data": q_result}, 200
        else:
            return {"status": True, "message": " You are not eligible for this subscription"}
    else:
        return {"status": False, "message": "No Records Found"}
