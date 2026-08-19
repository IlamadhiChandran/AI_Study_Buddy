import { useEffect, useRef, useState } from "react"
import "./App.css"

const API_URL = "http://127.0.0.1:8000"

function App() {
  const [selectedFile, setSelectedFile] = useState(null)
  const [uploadStatus, setUploadStatus] = useState("")
  const [isUploading, setIsUploading] = useState(false)
  const [question, setQuestion] = useState("")
  const [messages, setMessages] = useState([])
  const [isThinking, setIsThinking] = useState(false)
  const chatEndRef = useRef(null)

  useEffect(() => {
    chatEndRef.current?.scrollIntoView({
      behavior: "smooth",
    })
  }, [messages, isThinking])

  // Handle PDF selection
  const handleFileChange = (event) => {
    const file = event.target.files[0]

    if (!file) {
      return
    }

    if (file.type !== "application/pdf") {
      setUploadStatus("Please choose a PDF file.")
      setSelectedFile(null)
      return
    }

    setSelectedFile(file)
    setUploadStatus(file.name)
  }

  // Upload PDF to FastAPI
  const handleUpload = async () => {
    if (!selectedFile) {
      setUploadStatus("Please choose a PDF first.")
      return
    }

    setIsUploading(true)
    setUploadStatus("Uploading and processing...")

    const formData = new FormData()
    formData.append("file", selectedFile)

    try {
      const response = await fetch(`${API_URL}/upload`, {
        method: "POST",
        body: formData,
      })

      const data = await response.json()

      if (!response.ok) {
        throw new Error(data.detail || "Upload failed")
      }

      setUploadStatus(
        `${data.filename} uploaded successfully (${data.chunks_stored} chunks)`
      )

      setMessages([])

    } catch (error) {
      console.error(error)
      setUploadStatus(`Upload failed: ${error.message}`)
    } finally {
      setIsUploading(false)
    }
  }

  // Send question to FastAPI
  const handleSend = async (customQuestion = null) => {
    const questionToAsk = customQuestion || question.trim()

    if (!questionToAsk) {
      return
    }

    // Add user's question immediately
    setMessages((previous) => [
      ...previous,
      {
        type: "user",
        text: questionToAsk,
      },
    ])

    setQuestion("")
    setIsThinking(true)

    try {
      const response = await fetch(`${API_URL}/chat`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          question: questionToAsk,
        }),
      })

      const data = await response.json()

      if (!response.ok) {
        throw new Error(data.detail || "Something went wrong")
      }

      setMessages((previous) => [
        ...previous,
        {
          type: "ai",
          text: data.answer,
        },
      ])
    } catch (error) {
      console.error(error)

      setMessages((previous) => [
        ...previous,
        {
          type: "ai",
          text: "Sorry, I couldn't connect to the AI Study Buddy backend.",
        },
      ])
    } finally {
      setIsThinking(false)
    }
  }

  // Allow Enter key to send question
  const handleKeyDown = (event) => {
    if (event.key === "Enter") {
      handleSend()
    }
  }

  return (
    <div className="app">

      {/* Sidebar */}
      <aside className="sidebar">

        <div className="brand">
          <div className="brand-icon">📚</div>

          <div>
            <h1>Aster</h1>
            <span>Learn. Understand. Grow.</span>
          </div>
        </div>

        <nav>
          <button className="nav-item active">
            <span>💬</span>
            Study Chat
          </button>

          <button className="nav-item">
            <span>📄</span>
            My Material
          </button>

          <button className="nav-item">
            <span>⭐</span>
            Saved Notes
          </button>
        </nav>

        <div className="streak-card">
          <div className="streak-icon">★</div>

          <div>
            <strong>7 Day Streak</strong>
            <p>Keep going!</p>
          </div>
        </div>

      </aside>

      {/* Main content */}
      <main className="main">

        <header className="topbar">

          <div>
            <p className="eyebrow">WELCOME BACK</p>
            <h2>Ready to study?</h2>
          </div>

          <div className="profile">
            <span className="profile-dot"></span>
            Student
          </div>

        </header>

        <div className="content">

          {/* Upload section */}
          <section className="upload-card">

            <div className="section-icon">📄</div>

            <div className="upload-content">

              <p className="eyebrow">STUDY MATERIAL</p>

              <h3>Upload your PDF</h3>

              <p>
                Add your study material and let Aster help you understand it.
              </p>

              <div className="upload-actions">

                <input
                  type="file"
                  accept=".pdf"
                  id="pdf-upload"
                  onChange={handleFileChange}
                />

                <label
                  htmlFor="pdf-upload"
                  className="choose-btn"
                >
                  {selectedFile ? selectedFile.name : "Choose PDF"}
                </label>

                <button
                  className="upload-btn"
                  onClick={handleUpload}
                  disabled={!selectedFile || isUploading}
                >
                  {isUploading ? "Uploading..." : "Upload Material"}
                </button>
              </div>

              {uploadStatus && (
                <div className="upload-status">
                  {uploadStatus}
                </div>
              )}
            </div>
          </section>

          {/* Chat section */}
          <section className="chat-card">

            <div className="chat-header">

              <div>
                <p className="eyebrow">AI STUDY SESSION</p>
                <h3>Ask Aster</h3>
              </div>

              <div className="ai-status">
                <span></span>
                {isThinking ? "Thinking..." : "AI Ready"}
              </div>

            </div>

            <div className="chat-area">

            {messages.length === 0 ? (
              <div className="message ai-message">
                <div className="message-label">Aster</div>

                <div className="message-bubble">
                  Hi! Upload your study material and ask me anything about it. 📚
                </div>
              </div>
            ) : (
              messages.map((message, index) => (
                <div
                  key={index}
                  className={`message ${
                    message.type === "user"
                      ? "user-message"
                      : "ai-message"
                  }`}
                >
                  <div className="message-label">
                    {message.type === "user" ? "YOU" : "Aster"}
                  </div>

                  <div className="message-bubble">
                    {message.text}
                  </div>
                </div>
              ))
            )}

              {isThinking && (
                <div className="message ai-message">

                  <div className="message-label">
                    Aster
                  </div>

                  <div className="message-bubble">
                    Thinking...
                  </div>

                </div>
              )}

            </div>

            <div className="chat-input-area">

              <input
                type="text"
                value={question}
                onChange={(event) => setQuestion(event.target.value)}
                onKeyDown={handleKeyDown}
                placeholder="Ask anything about your study material..."
              />

              <button
                className="send-btn"
                onClick={() => handleSend()}
                disabled={isThinking}
              >
                Send
                <span>➜</span>
              </button>
            </div>
            <div className="quick-actions">

              <button
                onClick={() =>
                  handleSend(
                    "Summarize the important points from the uploaded study material."
                  )
                }
              >
                ✨ Summarize
              </button>

              <button
                onClick={() =>
                  handleSend(
                    "Explain the important concepts from the uploaded study material in simple terms."
                  )
                }
              >
                🧠 Explain simply
              </button>

              <button
                onClick={() =>
                  handleSend(
                    "Create a short quiz based on the uploaded study material."
                  )
                }
              >
                ⭐ Quiz me
              </button>
            </div>
          </section>
        </div>
      </main>
    </div>
  )
}
export default App