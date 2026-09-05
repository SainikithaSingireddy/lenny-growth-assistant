"use client";

interface Props {
  value: string;
  setValue: (value: string) => void;
}

export default function ModelSelector({ value, setValue }: Props) {
  return (
    <select
      value={value}
      onChange={(e) => setValue(e.target.value)}
      style={{
        padding: "8px 12px",
        borderRadius: 8,
        border: "1px solid #d1d5db",
        fontSize: 14
      }}
    >
      <option value="gemini">Gemini</option>
    </select>
  );
}