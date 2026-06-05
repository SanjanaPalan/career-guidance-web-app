from flask import Flask, render_template, request

app = Flask(__name__)

career_data = {

    "web": {
        "career": "Web Developer",

        "description":
        "Designs and develops websites and web applications.",

        "roadmap": [
            "Learn HTML",
            "Learn CSS",
            "Learn JavaScript",
            "Learn React",
            "Learn Node.js",
            "Build Projects",
            "Create Portfolio",
            "Apply for Jobs"
        ],

        "skills": [
            "HTML",
            "CSS",
            "JavaScript",
            "React",
            "Git"
        ],

        "salary":
        "₹4 LPA - ₹12 LPA",

        "resources": [
            {
                "name": "HTML Tutorial",
                "link": "https://www.w3schools.com/html/"
            },
            {
                "name": "CSS Tutorial",
                "link": "https://www.w3schools.com/css/"
            },
            {
                "name": "JavaScript Tutorial",
                "link": "https://www.w3schools.com/js/"
            },
            {
                "name": "freeCodeCamp",
                "link": "https://www.freecodecamp.org/"
            }
        ]
    },

    "data": {
        "career": "Data Analyst",

        "description":
        "Analyzes data to generate business insights.",

        "roadmap": [
            "Learn Excel",
            "Learn SQL",
            "Learn Python",
            "Learn Pandas",
            "Learn Power BI",
            "Build Dashboards",
            "Create Portfolio"
        ],

        "skills": [
            "Excel",
            "SQL",
            "Python",
            "Power BI"
        ],

        "salary":
        "₹5 LPA - ₹15 LPA",

        "resources": [
            {
                "name": "SQL Tutorial",
                "link": "https://www.w3schools.com/sql/"
            },
            {
                "name": "Python Tutorial",
                "link": "https://www.learnpython.org/"
            },
            {
                "name": "Pandas Documentation",
                "link": "https://pandas.pydata.org/docs/"
            }
        ]
    }

}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    name = request.form["name"]
    interest = request.form["interest"]

    selected = career_data.get(interest)

    return render_template(
        "result.html",
        name=name,
        selected=selected
    )


if __name__ == "__main__":
    app.run(debug=True)