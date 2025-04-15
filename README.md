<h1>Note-Taking Microservices</h1>

<p>This repository contains microservices for a note-taking application. Each microservice (add, delete, get, update) is containerized with Docker.</p>

<h2>Prerequisites</h2>
<ul>
  <li><a href="https://www.docker.com/get-started">Docker</a> installed</li>
  <li><a href="https://hub.docker.com/">Docker Hub</a> account</li>
  <li>Log in to Docker:
    <pre><code>docker login</code></pre>
  </li>
</ul>

<h2>Microservices</h2>
<p>Each microservice has its own folder. Follow the steps below for each one.</p>

<hr />

<h3>1. <strong>Add Note</strong></h3>
<pre><code>cd addNote
docker build -t &lt;your-docker-username&gt;/add-note:latest .
docker push &lt;your-docker-username&gt;/add-note:latest
cd ..
</code></pre>

<hr />

<h3>2. <strong>Delete Note</strong></h3>
<pre><code>cd deleteNote
docker build -t &lt;your-docker-username&gt;/delete-note:latest .
docker push &lt;your-docker-username&gt;/delete-note:latest
cd ..
</code></pre>

<hr />

<h3>3. <strong>Get Note</strong></h3>
<pre><code>cd getNote
docker build -t &lt;your-docker-username&gt;/get-note:latest .
docker push &lt;your-docker-username&gt;/get-note:latest
cd ..
</code></pre>

<hr />

<h3>4. <strong>Update Note</strong></h3>
<pre><code>cd updateNote
docker build -t &lt;your-docker-username&gt;/update-note:latest .
docker push &lt;your-docker-username&gt;/update-note:latest
cd ..
</code></pre>

<hr />

<h2>Notes</h2>
<ul>
  <li>Ensure the <code>Dockerfile</code>, <code>requirements.txt</code>, and source code (<code>*.py</code>) are present in each service directory.</li>
  <li>If using private Docker Hub repositories, ensure access permissions are configured correctly.</li>
</ul>

<hr />

<h2>License</h2>
<p>MIT</p>
