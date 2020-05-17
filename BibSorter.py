
class BibSorter():
    author_list = []
    bibliography = {}

    def get_authors(self, s: str):
        if s == None: return
        # new_authors_list = [author.strip() for author in s.split(',') if author.strip() not in current]
        for author in s.split(','):
            tmp = author.strip()
            if tmp not in self.author_list:
                self.author_list.append(tmp)

    def add_to_authorlist(self, line: str):
        # Skip commented sections of a line
        if '%' in line:
            line = line[:line.find('%')]

        # Find the first instance of \cite cmd in the file and loop while there are still some
        idx_start = line.find('\\cite{')


        while idx_start != -1:
            # Find the end of the \cite to mark where authors are listed and extract them into a list using 'get_authors'
            idx_end = line.find('}', idx_start)
            self.get_authors(line[idx_start + 6:idx_end])
            # Slice the string in order to find the next instance of \cite and keep going
            line = line[idx_end + 1:]
            idx_start = line.find('\\cite{')



    def add_bibitem(self, bibitem: str):
        # Remove commented sections of each line
        bibitem = bibitem.strip().split('\n')
        bibitem = '\n'.join([line[:line.find('%')] if '%' in line else line for line in bibitem])
        idx_start = bibitem.find('{')
        idx_end = bibitem.find('}', idx_start)
        name = bibitem[idx_start + 1:idx_end]
        description = bibitem[idx_end + 1:]
        if name in self.author_list:
            self.bibliography[name] = description.strip()


    def extract_bibliography(self, old_bib: str):
        idx_start = old_bib.find('\\bibitem')
        old_bib = old_bib[idx_start + 1:] + '\\bibitem'
        # print(idx_start)
        while idx_start != -1:
            idx_end = old_bib.find('\\bibitem')
            self.add_bibitem(old_bib[:idx_end])
            old_bib = old_bib[idx_end + 1:]
            idx_start = old_bib.find('\\bibitem')






    def sort(self, file: str) -> list:
        orig_bib = ''
        with open(file, encoding="utf8") as orig_file, open(file[:-4] + '_copy.tex', 'w', encoding="utf8") as write_file:
            for line in orig_file:
                write_file.write(line)
                if '\\begin{thebibliography' in line:
                    break
                self.add_to_authorlist(line)
            for line in orig_file:
                if '\\end{thebibliography' in line:
                    break
                orig_bib += line
            self.extract_bibliography(orig_bib)
            for idx, author in enumerate(self.author_list):
              # print(idx, author)
              if author in self.author_list:
                  entry = f'\n% {str(idx + 1)}\n\\bibitem{{{author}}}\n{self.bibliography[author]}'
                  print(entry)

                  write_file.write(entry)
            write_file.write('\n\\end{{thebibliography}}')
            for line in orig_file:
                write_file.write(line)
        orig_file.close()
        write_file.close()
        return self.author_list
