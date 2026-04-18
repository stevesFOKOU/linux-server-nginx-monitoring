def app(environ, start_response):
    start_response("200 OK", [("Content-Type", "text/html")])

    html = """
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <title>Serveur Linux Project</title>
        <style>
            body {
                margin: 0;
                font-family: Arial, sans-serif;
                background: #0f172a;
                color: #e2e8f0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }

            .container {
                text-align: center;
                padding: 40px;
                background: #1e293b;
                border-radius: 12px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.5);
                max-width: 600px;
            }

            h1 {
                color: #38bdf8;
                margin-bottom: 10px;
            }

            p {
                font-size: 18px;
                line-height: 1.6;
                color: #cbd5e1;
            }

            .badge {
                display: inline-block;
                margin-top: 15px;
                padding: 5px 10px;
                background: #22c55e;
                color: black;
                border-radius: 6px;
                font-weight: bold;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 Serveur Linux en production</h1>
            <p>
                Reverse Proxy <b>Nginx</b> + Backend <b>Gunicorn</b><br>
                Architecture déployée sur Ubuntu Server
            </p>

            <div class="badge">STATUS: OK</div>
        </div>
    </body>
    </html>
    """

    return [html.encode("utf-8")]
