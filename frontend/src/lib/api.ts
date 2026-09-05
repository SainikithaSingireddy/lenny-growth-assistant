const BASE =
  process.env.NEXT_PUBLIC_API_URL || "http://127.0.0.1:8000";

export async function askQuestion(message: string, provider = "gemini") {
  const res = await fetch(`${BASE}/chat/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ message, provider }),
  });

  if (!res.ok) throw new Error("Backend error");

  return res.json();
}