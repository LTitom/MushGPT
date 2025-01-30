import React, { useState } from 'react';
import { Send, Sprout } from 'lucide-react';

function App() {
  const [message, setMessage] = useState('');
  const [chatHistory, setChatHistory] = useState<Array<{ type: 'user' | 'bot'; text: string }>>([]);
  const [isLoading, setIsLoading] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!message.trim()) return;

    // Add user message to chat
    setChatHistory(prev => [...prev, { type: 'user', text: message }]);
    setIsLoading(true);

    try {
      const response = await fetch('/query/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query_text: message }),
      });

      const data = await response.json();
      setChatHistory(prev => [...prev, { type: 'bot', text: data.response }]);
    } catch (error) {
      console.error('Error:', error);
      setChatHistory(prev => [...prev, { type: 'bot', text: "Désolé, j'ai rencontré une erreur. Veuillez réessayer plus tard." }]);
    }

    setIsLoading(false);
    setMessage('');
  };

  return (
    <div className="min-h-screen bg-custom-dark text-white">
      {/* Header */}
      <header className="border-b border-gray-800 p-4">
        <div className="max-w-4xl mx-auto flex items-center gap-3">
          <Sprout className="w-8 h-8 text-green-400" />
          <h1 className="text-xl font-semibold">MushGPT v1.0</h1>
        </div>
      </header>

      {/* Main Content */}
      <main className="max-w-4xl mx-auto p-4 flex flex-col h-[calc(100vh-80px)]">
        {/* Welcome Message */}
        {chatHistory.length === 0 && (
          <div className="flex-1 flex flex-col items-center justify-center text-center">
            <Sprout className="w-16 h-16 text-green-400 mb-6" />
            <h2 className="text-3xl font-bold mb-4">
              Comment puis-je vous aider à accélérer la transition écologique ?
            </h2>
            <p className="text-gray-400 max-w-lg">
              Posez vos questions sur l'environnement, le développement durable, et les actions écologiques.
            </p>
          </div>
        )}

        {/* Chat Messages */}
        {chatHistory.length > 0 && (
          <div className="flex-1 overflow-y-auto mb-4 space-y-4">
            {chatHistory.map((msg, index) => (
              <div
                key={index}
                className={`flex ${msg.type === 'user' ? 'justify-end' : 'justify-start'}`}
              >
                <div
                  className={`max-w-[80%] rounded-lg p-4 ${
                    msg.type === 'user'
                      ? 'bg-green-600 text-white'
                      : 'bg-gray-800 text-white'
                  }`}
                >
                  {msg.text}
                </div>
              </div>
            ))}
            {isLoading && (
              <div className="flex justify-start">
                <div className="bg-gray-800 text-white rounded-lg p-4">
                  <div className="flex space-x-2">
                    <div className="w-2 h-2 bg-gray-500 rounded-full animate-bounce" />
                    <div className="w-2 h-2 bg-gray-500 rounded-full animate-bounce" style={{ animationDelay: '0.2s' }} />
                    <div className="w-2 h-2 bg-gray-500 rounded-full animate-bounce" style={{ animationDelay: '0.4s' }} />
                  </div>
                </div>
              </div>
            )}
          </div>
        )}

        {/* Input Form */}
        <form onSubmit={handleSubmit} className="flex gap-2">
          <input
            type="text"
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            placeholder="Que voulez-vous apprendre, faire, trouver ?"
            className="flex-1 bg-gray-800 text-white rounded-lg px-4 py-3 focus:outline-none focus:ring-2 focus:ring-green-500"
          />
          <button
            type="submit"
            disabled={isLoading}
            className="bg-green-600 text-white p-3 rounded-lg hover:bg-green-700 transition-colors disabled:opacity-50"
          >
            <Send className="w-6 h-6" />
          </button>
        </form>

        {/* Footer */}
        <p className="text-center text-gray-500 text-sm mt-4">
          MushGPT peut faire des erreurs. Vérifiez les informations importantes par vous-même
        </p>
      </main>
    </div>
  );
}

export default App;