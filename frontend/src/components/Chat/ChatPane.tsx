"use client";

import { useState } from "react";
import MessageItem from "./MessageItem";
import ModelSelector from "./ModelSelector";
import { askQuestion } from "../../lib/api";

interface Props {
  onArtifact: (html: string) => void;
}

interface ChatMessage {
  role: "user" | "assistant";
  content: string;
}

export default function ChatPane({ onArtifact }: Props) {
  const [provider, setProvider] = useState("ollama");
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);

  const [messages, setMessages] = useState<ChatMessage[]>([]);

  async function handleSend(question?: string) {
    const message = question ?? input;

    if (!message.trim()) return;

    setMessages((prev) => [
      ...prev,
      { role: "user", content: message }
    ]);

    setInput("");
    setLoading(true);

    try {
      const data = await askQuestion(message, provider);

      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          content: data.answer
        }
      ]);

      if (data.artifact_html) {
        onArtifact(data.artifact_html);
      }
    } catch {
      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          content: "Unable to connect to the backend."
        }
      ]);
    }

    setLoading(false);
  }

  const suggestedQuestions = [
    "How did Airbnb improve onboarding?",
    "What activation metrics did the guest recommend?",
    "How did the team reduce signup friction?"
  ];

  return (
    <div
      style={{
        display: "flex",
        flexDirection: "column",
        height: "100%"
      }}
    >
      {/* Header */}
      <div
        style={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          marginBottom: 16
        }}
      >
        <div>
          <h2 style={{ margin: 0 }}>Chat Assistant</h2>
          <p
            style={{
              margin: "4px 0",
              color: "#64748b",
              fontSize: 14
            }}
          >
            Ask questions about Lenny's podcast
          </p>
        </div>

        <ModelSelector value={provider} setValue={setProvider} />
      </div>

      {/* Messages */}
      <div
        style={{
          flex: 1,
          minHeight: 430,
          maxHeight: 430,
          overflowY: "auto",
          border: "1px solid #e5e7eb",
          borderRadius: 12,
          padding: 16,
          background: "#f8fafc"
        }}
      >
        {messages.length === 0 ? (
          <div
            style={{
              textAlign: "center",
              marginTop: 40
            }}
          >
            <h3 style={{ marginBottom: 8 }}>
              Welcome to Lenny Growth Assistant
            </h3>

            <p style={{ color: "#64748b" }}>
              Search across podcast transcripts using natural language.
            </p>

            <div
              style={{
                marginTop: 24,
                display: "flex",
                flexDirection: "column",
                gap: 10
              }}
            >
              {suggestedQuestions.map((q, i) => (
                <button
                  key={i}
                  onClick={() => handleSend(q)}
                  style={{
                    textAlign: "left",
                    padding: 12,
                    borderRadius: 10,
                    border: "1px solid #dbe4f0",
                    background: "white",
                    cursor: "pointer"
                  }}
                >
                  {q}
                </button>
              ))}
            </div>
          </div>
        ) : (
          messages.map((msg, index) => (
            <MessageItem
              key={index}
              role={msg.role}
              content={msg.content}
            />
          ))
        )}

        {loading && (
          <div
            style={{
              marginTop: 10,
              color: "#64748b",
              fontStyle: "italic"
            }}
          >
            Assistant is thinking...
          </div>
        )}
      </div>

      {/* Input */}
      <textarea
        rows={4}
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="Ask about onboarding, pricing, growth, retention..."
        style={{
          width: "100%",
          marginTop: 16,
          padding: 12,
          borderRadius: 10,
          border: "1px solid #d1d5db",
          resize: "none",
          fontSize: 15
        }}
      />

      <button
        onClick={() => handleSend()}
        disabled={loading}
        style={{
          marginTop: 12,
          padding: "12px 18px",
          background: loading ? "#94a3b8" : "#2563eb",
          color: "white",
          border: "none",
          borderRadius: 10,
          fontWeight: 600,
          cursor: loading ? "not-allowed" : "pointer"
        }}
      >
        {loading ? "Generating..." : "Ask Assistant"}
      </button>
    </div>
  );
}