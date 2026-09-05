const BASE = "http://127.0.0.1:8000";

export async function askQuestion(
  message: string,
  provider: string
){
  const res = await fetch(`${BASE}/chat/`,{
    method:"POST",
    headers:{
      "Content-Type":"application/json"
    },
    body:JSON.stringify({
      session_id:1,
      message,
      provider
    })
  });

  return await res.json();
}