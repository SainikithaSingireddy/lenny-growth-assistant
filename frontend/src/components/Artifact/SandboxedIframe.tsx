interface Props {
  html: string;
}

export default function SandboxedIframe({ html }: Props) {
  if (!html) {
    return (
      <div
        style={{
          height: 320,
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
          color: "#64748b",
          border: "1px dashed #cbd5e1",
          borderRadius: 10,
        }}
      >
        No artifact generated yet
      </div>
    );
  }

  return (
    <iframe
      title="artifact-viewer"
      srcDoc={html}
      sandbox="allow-same-origin"
      style={{
        width: "100%",
        height: 320,
        border: "1px solid #e5e7eb",
        borderRadius: 10,
        background: "white",
      }}
    />
  );
}