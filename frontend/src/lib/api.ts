const BASE =
  process.env.NEXT_PUBLIC_API_URL ?? "http://127.0.0.1:8000";

export async function askQuestion(
  message: string,
  provider: string = "ollama"
) {
  const response = await fetch(`${BASE}/chat/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      message,
      provider,
    }),
  });

  if (!response.ok) {
    throw new Error("Failed to connect to backend");
  }

  return response.json();
}