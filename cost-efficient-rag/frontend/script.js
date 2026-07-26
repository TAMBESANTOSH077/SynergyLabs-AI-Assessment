const uploadBtn = document.getElementById("uploadBtn");
const pdfInput = document.getElementById("pdfInput");

const askBtn = document.getElementById("askBtn");

const answer = document.getElementById("answer");
const sources = document.getElementById("sources");

const uploadedFiles = document.getElementById("uploadedFiles");

// Sidebar Upload Button
uploadBtn.addEventListener("click", () => {
    pdfInput.click();
});

// Upload PDF
pdfInput.addEventListener("change", uploadPDF);

async function uploadPDF() {

    const file = pdfInput.files[0];

    if (!file) return;

    const formData = new FormData();
    formData.append("file", file);

    answer.innerHTML = "📄 Uploading PDF...";

    uploadBtn.disabled = true;

    try {

        const response = await fetch("/ingest", {
            method: "POST",
            body: formData
        });

        if (!response.ok) {
            throw new Error("Upload Failed");
        }

        const data = await response.json();

        answer.innerHTML = "✅ PDF uploaded successfully.";

        uploadedFiles.innerHTML += `
        <div class="file-card">

            <div>

                <i class="fa-solid fa-file-pdf" style="color:red"></i>

                <strong>${file.name}</strong>

                <small>Indexed</small>

            </div>

            <button class="delete-btn">
                <i class="fa-solid fa-trash"></i>
            </button>

        </div>
        `;

        updateCount();
        attachDeleteEvents();

        // Optional if backend returns chunks
        if (data.total_chunks) {
            document.getElementById("chunkCount").innerText = data.total_chunks;
        }

        pdfInput.value = "";

    } catch (err) {

        console.error(err);

        answer.innerHTML = "❌ Upload Failed";

    } finally {

        uploadBtn.disabled = false;

    }

}

// Ask Question

askBtn.addEventListener("click", askQuestion);

async function askQuestion() {

    const question = document.getElementById("question").value.trim();

    if (!question) {
        alert("Enter your question.");
        return;
    }

    answer.innerHTML = "🤖 AI is thinking...";
    sources.innerHTML = "";

    askBtn.disabled = true;

    const start = performance.now();

    try {

        const response = await fetch("/query", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                query: question,
                top_k: 5
            })

        });

        if (!response.ok) {
            throw new Error("Server Error");
        }

        if(!response.ok){

    const txt = await response.text();

    throw new Error(txt);

}

const data = await response.json();

        answer.innerHTML = data.answer || "No answer returned.";

        if (Array.isArray(data.sources) && data.sources.length > 0) {

            data.sources.forEach(src => {

                sources.innerHTML += `
                <div class="source">

                    📄 <strong>${src.source}</strong><br>

                    Chunk ${src.chunk}

                </div>
                `;

            });

        } else {

            sources.innerHTML = "No sources found.";

        }

    }

    catch(err){

    console.error("Query Error:", err);

    answer.innerHTML = `
        <span style="color:red;">
            ❌ ${err.message}
        </span>
    `;

}

    finally {

        askBtn.disabled = false;

        const end = performance.now();

        document.getElementById("latency").innerText =
            ((end - start) / 1000).toFixed(2) + " sec";

    }

}
// Delete Uploaded PDF

function attachDeleteEvents() {

    document.querySelectorAll(".delete-btn").forEach(btn => {

        btn.onclick = function () {

            this.closest(".file-card").remove();

            updateCount();

        };

    });

}

// Update Counter

function updateCount() {

    const total = document.querySelectorAll(".file-card").length;

    document.getElementById("docCount").innerText = total;
    document.getElementById("totalDocs").innerText = total;

}


const dropArea = document.getElementById("dropArea");

dropArea.addEventListener("dragover",(e)=>{
    e.preventDefault();
});

dropArea.addEventListener("drop",(e)=>{
    e.preventDefault();

    pdfInput.files = e.dataTransfer.files;

    uploadPDF();
});