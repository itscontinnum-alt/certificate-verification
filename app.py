from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <h1>Birth Certificate Verification</h1>
    <p>Use the verification link provided with your certificate.</p>
    """


@app.route("/verify/<certificate_id>")
def verify(certificate_id):

    # Certificate information
    name = "Mahira Vashist"
    event = "BIRTH"
    application_no = "0124-12406219915"
    submit_date = "31/10/2024"
    event_date = "25/10/2024"
    status = "Certificate Generated"

    return f"""
    <!DOCTYPE html>
    <html>
    <head>

        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <title>Certificate Details</title>

        <style>

            body {{
                margin: 0;
                font-family: Arial, sans-serif;
                background: #eef1f7;
            }}

            .container {{
                max-width: 650px;
                margin: 30px auto;
                padding: 15px;
            }}

            .title {{
                background: #168bd0;
                color: white;
                text-align: center;
                padding: 20px;
                font-size: 28px;
                font-weight: bold;
                border-radius: 8px 8px 0 0;
            }}

            table {{
                width: 100%;
                border-collapse: collapse;
                background: white;
            }}

            td {{
                border: 1px solid #ddd;
                padding: 18px;
                font-size: 18px;
            }}

            td:first-child {{
                width: 35%;
                background: #f5f5f5;
                font-weight: bold;
            }}

            .button {{
                display: inline-block;
                padding: 12px 25px;
                margin: 5px;
                color: white;
                text-decoration: none;
                border-radius: 20px;
                font-weight: bold;
            }}

            .download {{
                background: #4caf50;
            }}

            .view {{
                background: #28b6dc;
            }}

            .footer {{
                margin-top: 100px;
                background: #07559b;
                color: white;
                text-align: center;
                padding: 30px 10px;
            }}

            @media (max-width: 600px) {{

                .container {{
                    margin: 10px;
                    padding: 5px;
                }}

                .title {{
                    font-size: 22px;
                }}

                td {{
                    font-size: 16px;
                    padding: 14px;
                }}

            }}

        </style>

    </head>

    <body>

        <div class="container">

            <div class="title">
                Certificate Details
            </div>

            <table>

                <tr>
                    <td>Name:</td>
                    <td>{name}</td>
                </tr>

                <tr>
                    <td>Event:</td>
                    <td>{event}</td>
                </tr>

                <tr>
                    <td>Application No.:</td>
                    <td>{application_no}</td>
                </tr>

                <tr>
                    <td>Submit Date:</td>
                    <td>{submit_date}</td>
                </tr>

                <tr>
                    <td>Event Date:</td>
                    <td>{event_date}</td>
                </tr>

                <tr>
                    <td>Status:</td>
                    <td>{status}</td>
                </tr>

                <tr>
                    <td>Action:</td>
                    <td>

                        <a href="#" class="button download">
                            ⬇ DOWNLOAD
                        </a>

                        <a href="#" class="button view">
                            👁 VIEW
                        </a>

                    </td>
                </tr>

            </table>

        </div>

        <div class="footer">

            <h2>Disclaimer</h2>

            <p>
                This website provides certificate verification
                information.
            </p>

            <p>
                Copyright © 2026
            </p>

        </div>

    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(debug=True)