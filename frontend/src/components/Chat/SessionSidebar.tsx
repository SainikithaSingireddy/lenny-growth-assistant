"use client";

import { useEffect, useState } from "react";

interface Session {
  id: number;
  title: string;
}

export default function SessionSidebar() {
  const [sessions, setSessions] = useState<Session[]>([]);
  const [activeId, setActiveId] = useState<number | null>(null);

  async function loadSessions() {
    const res = await fetch("http://127.0.0.1:8000/sessions/");
    const data = await res.json();

    setSessions(data);

    if (data.length > 0 && activeId === null) {
      setActiveId(data[0].id);
    }
  }

  async function createSession() {
    const res = await fetch("http://127.0.0.1:8000/sessions/", {
      method: "POST",
    });

    const newSession = await res.json();

    await loadSessions();

    setActiveId(newSession.id);
  }

  useEffect(() => {
    async function initialize() {
      const res = await fetch("http://127.0.0.1:8000/sessions/");
      const data = await res.json();

      // Create one session only if database is empty
      if (data.length === 0) {
        await fetch("http://127.0.0.1:8000/sessions/", {
          method: "POST",
        });
      }

      await loadSessions();
    }

    initialize();
  }, []);

  return (
    <div>
      <button
        onClick={createSession}
        style={{
          width: "100%",
          padding: "10px",
          borderRadius: 8,
          border: "none",
          background: "#2563eb",
          color: "white",
          fontWeight: 600,
          cursor: "pointer",
          marginBottom: 16,
        }}
      >
        + New Chat
      </button>

      <div style={{ display: "flex", flexDirection: "column", gap: 8 }}>
        {sessions.map((session) => (
          <div
            key={session.id}
            onClick={() => setActiveId(session.id)}
            style={{
              padding: 10,
              borderRadius: 8,
              cursor: "pointer",
              background:
                activeId === session.id ? "#DBEAFE" : "#F8FAFC",
              border:
                activeId === session.id
                  ? "1px solid #2563eb"
                  : "1px solid #E5E7EB",
              fontWeight: activeId === session.id ? 600 : 400,
            }}
          >
            💬 {session.title}
          </div>
        ))}
      </div>
    </div>
  );
}