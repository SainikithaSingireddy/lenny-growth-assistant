"use client";

import { useState } from "react";

import ChatPane from "../components/Chat/ChatPane";
import SessionSidebar from "../components/Chat/SessionSidebar";
import ArtifactViewer from "../components/Artifact/ArtifactViewer";

export default function Home() {
  const [artifact, setArtifact] = useState("");

  return (
    <main
      style={{
        minHeight: "100vh",
        background: "#eef3f8",
        padding: 24,
      }}
    >
      <div
        style={{
          maxWidth: 1400,
          margin: "0 auto",
        }}
      >
        <div style={{ marginBottom: 20 }}>
          <h1 style={{ margin: 0 }}>Lenny Growth Assistant</h1>

          <p style={{ color: "#64748b" }}>
            Enterprise RAG Assistant powered by FastAPI, PostgreSQL, pgvector &
            Gemini
          </p>
        </div>

        <div
          style={{
            display: "grid",
            gridTemplateColumns: artifact
              ? "250px 2fr 1fr"
              : "250px 1fr",
            gap: 20,
          }}
        >
          {/* Sidebar */}
          <div
            style={{
              background: "white",
              borderRadius: 14,
              padding: 18,
            }}
          >
            <h3>Sessions</h3>
            <SessionSidebar />
          </div>

          {/* Chat */}
          <div
            style={{
              background: "white",
              borderRadius: 14,
              padding: 18,
            }}
          >
            <ChatPane onArtifact={setArtifact} />
          </div>

          {/* Artifact Viewer - Only show when an artifact exists */}
          {artifact && (
            <div
              style={{
                background: "white",
                borderRadius: 14,
                padding: 18,
              }}
            >
              <ArtifactViewer html={artifact} />
            </div>
          )}
        </div>
      </div>
    </main>
  );
}