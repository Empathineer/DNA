<h1 id="dna"><a data-id="" href="#dna">DNA</a></h1>
<p>Implement a program that identifies a person based on their DNA, per the criteria below.</p>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>$ python dna.py databases/large.csv sequences/5.txt
Lavender
</code></pre></div></div>

<h2 id="background"><a data-id="" href="#background">Background</a></h2>


<p>DNA, the carrier of genetic information in living things, has been used in criminal justice for decades. But how, exactly, does DNA profiling work? Given a sequence of DNA, how can forensic investigators identify to whom it belongs?</p>

<p>Well, DNA is really just a sequence of molecules called nucleotides, arranged into a particular shape (a double helix). Each nucleotide of DNA contains one of four different bases: adenine (A), cytosine (C), guanine (G), or thymine (T). Every human cell has billions of these nucleotides arranged in sequence. Some portions of this sequence (i.e. genome) are the same, or at least very similar, across almost all humans, but other portions of the sequence have a higher genetic diversity and thus vary more across the population.</p>

<p>One place where DNA tends to have high genetic diversity is in Short Tandem Repeats (STRs). An STR is a short sequence of DNA bases that tends to repeat consecutively numerous times at specific locations inside of a person’s DNA. The number of times any particular STR repeats varies a lot among individuals. In the DNA samples below, for example, Alice has the STR <code class="highlighter-rouge">AGAT</code> repeated four times in her DNA, while Bob has the same STR repeated five times.</p>


<p>Using multiple STRs, rather than just one, can improve the accuracy of DNA profiling. If the probability that two people have the same number of repeats for a single STR is 5%, and the analyst looks at 10 different STRs, then the probability that two DNA samples match purely by chance is about 1 in 1 quadrillion (assuming all STRs are independent of each other). So if two DNA samples match in the number of repeats for each of the STRs, the analyst can be pretty confident they came from the same person. CODIS, The FBI’s <a href="https://www.fbi.gov/services/laboratory/biometric-analysis/codis/codis-and-ndis-fact-sheet">DNA database</a>, uses 20 different STRs as part of its DNA profiling process.</p>

<p>What might such a DNA database look like? Well, in its simplest form, you could imagine formatting a DNA database as a CSV file, wherein each row corresponds to an individual, and each column corresponds to a particular STR.</p>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>name,AGAT,AATG,TATC
Alice,28,42,14
Bob,17,22,19
Charlie,36,18,25
</code></pre></div></div>

<p>The data in the above file would suggest that Alice has the sequence <code class="highlighter-rouge">AGAT</code> repeated 28 times consecutively somewhere in her DNA, the sequence <code class="highlighter-rouge">AATG</code> repeated 42 times, and <code class="highlighter-rouge">TATC</code> repeated 14 times. Bob, meanwhile, has those same three STRs repeated 17 times, 22 times, and 19 times, respectively. And Charlie has those same three STRs repeated 36, 18, and 25 times, respectively.</p>

<p>So given a sequence of DNA, how might you identify to whom it belongs? Well, imagine that you looked through the DNA sequence for the longest consecutive sequence of repeated <code class="highlighter-rouge">AGAT</code>s and found that the longest sequence was 17 repeats long. If you then found that the longest sequence of <code class="highlighter-rouge">AATG</code> is 22 repeats long, and the longest sequence of <code class="highlighter-rouge">TATC</code> is 19 repeats long, that would provide pretty good evidence that the DNA was Bob’s. Of course, it’s also possible that once you take the counts for each of the STRs, it doesn’t match anyone in your DNA database, in which case you have no match.</p>

<p>In practice, since analysts know on which chromosome and at which location in the DNA an STR will be found, they can localize their search to just a narrow section of DNA. But we’ll ignore that detail for this problem.</p>

<p>Your task is to write a program that will take a sequence of DNA and a CSV file containing STR counts for a list of individuals and then output to whom the DNA (most likely) belongs.</p>

<h2 id="specification"><a data-id="" href="#specification">Specification</a></h2>

<p>In a file called <code class="highlighter-rouge">dna.py</code> in <code class="highlighter-rouge">~/pset6/dna/</code>, implement a program that identifies to whom a sequence of DNA belongs.</p>

<ul class="fa-ul">
  <li data-marker="*"><span class="fa-li"><i class="fas fa-circle"></i></span>The program should require as its first command-line argument the name of a CSV file containing the STR counts for a list of individuals and should require as its second command-line argument the name of a text file containing the DNA sequence to identify.
    <ul class="fa-ul">
      <li data-marker="*"><span class="fa-li"><i class="fas fa-circle"></i></span>If your program is executed with the incorrect number of command-line arguments, your program should print an error message of your choice (with <code class="highlighter-rouge">print</code>). If the correct number of arguments are provided, you may assume that the first argument is indeed the filename of a valid CSV file, and that the second argument is the filename of a valid text file.</li>
    </ul>
  </li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-circle"></i></span>Your program should open the CSV file and read its contents into memory.
    <ul class="fa-ul">
      <li data-marker="*"><span class="fa-li"><i class="fas fa-circle"></i></span>You may assume that the first row of the CSV file will be the column names. The first column will be the word <code class="highlighter-rouge">name</code> and the remaining columns will be the STR sequences themselves.</li>
    </ul>
  </li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-circle"></i></span>Your program should open the DNA sequence and read its contents into memory.</li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-circle"></i></span>For each of the STRs (from the first line of the CSV file), your program should compute the longest run of consecutive repeats of the STR in the DNA sequence to identify.</li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-circle"></i></span>If the STR counts match exactly with any of the individuals in the CSV file, your program should print out the name of the matching individual.
    <ul class="fa-ul">
      <li data-marker="*"><span class="fa-li"><i class="fas fa-circle"></i></span>You may assume that the STR counts will not match more than one individual.</li>
      <li data-marker="*"><span class="fa-li"><i class="fas fa-circle"></i></span>If the STR counts do not match exactly with any of the individuals in the CSV file, your program should print <code class="highlighter-rouge">"No match"</code>.</li>
    </ul>
  </li>
</ul>


<h2 id="usage"><a data-id="" href="#usage">Usage</a></h2>

<p>Your program should behave per the example below:</p>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>$ python dna.py databases/large.csv sequences/5.txt
Lavender
</code></pre></div></div>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>$ python dna.py
Usage: python dna.py data.csv sequence.txt
</code></pre></div></div>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>$ python dna.py data.csv
Usage: python dna.py data.csv sequence.txt
</code></pre></div></div>

<h2 id="getting-started"><a data-id="" href="#getting-started">Getting Started</a></h2>

<p>Here’s how to download this problem into your own CS50 IDE. Log into <a href="https://ide.cs50.io/">CS50 IDE</a> and then, in a terminal window, execute each of the below.</p>

<ul class="fa-ul">
  <li data-marker="*"><span class="fa-li"><i class="fas fa-circle"></i></span>Execute <code class="highlighter-rouge">cd</code> to ensure that you’re in <code class="highlighter-rouge">~/</code> (i.e., your home directory, aka <code class="highlighter-rouge">~</code>).</li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-circle"></i></span>If you haven’t already, execute <code class="highlighter-rouge">mkdir pset6</code> to make (i.e., create) a directory called <code class="highlighter-rouge">pset6</code> in your home directory.</li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-circle"></i></span>Execute <code class="highlighter-rouge">cd pset6</code> to change into (i.e., open) that directory.</li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-circle"></i></span>Execute <code class="highlighter-rouge">wget https://cdn.cs50.net/2019/fall/psets/6/dna/dna.zip</code> to download a (compressed) ZIP file with this problem’s distribution.</li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-circle"></i></span>Execute <code class="highlighter-rouge">unzip dna.zip</code> to uncompress that file.</li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-circle"></i></span>Execute <code class="highlighter-rouge">rm dna.zip</code> followed by <code class="highlighter-rouge">yes</code> or <code class="highlighter-rouge">y</code> to delete that ZIP file.</li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-circle"></i></span>Execute <code class="highlighter-rouge">ls</code>. You should see a directory called <code class="highlighter-rouge">dna</code>, which was inside of that ZIP file.</li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-circle"></i></span>Execute <code class="highlighter-rouge">cd dna</code> to change into that directory.</li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-circle"></i></span>Execute <code class="highlighter-rouge">ls</code>. You should see a directory of sample <code class="highlighter-rouge">databases</code> and a directory of sample <code class="highlighter-rouge">sequences</code>.</li>
</ul>


<h2 id="hints"><a data-id="" href="#hints">Hints</a></h2>

<ul class="fa-ul">
  <li data-marker="*"><span class="fa-li"><i class="fas fa-circle"></i></span>You may find Python’s <a href="https://docs.python.org/3/library/csv.html"><code class="highlighter-rouge">csv</code></a> module helpful for reading CSV files into memory. You may want to take advantage of either <a href="https://docs.python.org/3/library/csv.html#csv.reader"><code class="highlighter-rouge">csv.reader</code></a> or <a href="https://docs.python.org/3/library/csv.html#csv.DictReader"><code class="highlighter-rouge">csv.DictReader</code></a>.</li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-circle"></i></span>The <a href="https://docs.python.org/3.3/tutorial/inputoutput.html#reading-and-writing-files"><code class="highlighter-rouge">open</code></a> and <a href="https://docs.python.org/3.3/tutorial/inputoutput.html#methods-of-file-objects"><code class="highlighter-rouge">read</code></a> functions may prove useful for reading text files into memory.</li>
  <li data-marker="*"><span class="fa-li"><i class="fas fa-circle"></i></span>Consider what data structures might be helpful for keeping tracking of information in your program. A <a href="https://docs.python.org/3/tutorial/introduction.html#lists"><code class="highlighter-rouge">list</code></a> or a <a href="https://docs.python.org/3/tutorial/datastructures.html#dictionaries"><code class="highlighter-rouge">dict</code></a> may prove useful.</li>
</ul>




