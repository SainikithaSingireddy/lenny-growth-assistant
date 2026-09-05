def generate_html(title: str, content: str):
    return f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
body {{
font-family: Arial;
padding:40px;
background:#ffffff;
}}
h1 {{
color:#2563eb;
}}
.card {{
padding:20px;
border-radius:10px;
background:#eef4ff;
}}
</style>
</head>
<body>

<h1>{title}</h1>

<div class="card">
{content}
</div>

</body>
</html>
"""