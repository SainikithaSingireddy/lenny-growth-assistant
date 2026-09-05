def generate_html(title: str, body: str):
    return f"""
<!DOCTYPE html>
<html>
<head>
<title>{title}</title>
</head>
<body>
<h1>{title}</h1>
<p>{body}</p>
</body>
</html>
"""