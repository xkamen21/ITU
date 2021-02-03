# ITU

### PC verze aplikace - překlad
#### Instalace potřebných balíčků
1. přesuňte se do složky "PC_ITUsportsTracker"
2. spusťte příkaz "sudo pip3 install pyqt5" pro instalaci modulu PyQt5
3. spusťte příkaz "sudo pip3 install pyqtgraph" pro instalaci modulu PyQt5
4. pokud používáte jiné prostředí jako například Anaconda spusťte instalaci pomocí vašeho prostředí
	pro condu zadejte příkaz "conda install -c conda-forge pyqtgraph"

#### Spuštění
1. pro spuštění zadejte příkaz "python3 ITUsportsTracker.py"

#### O projektu    
- projekt je zaměřen na uživatelské rozhraní
- Hlavní modul: ITUSportsTracker.py
- Vedlejší moduly: GuiStyles.py, GuiHandler.py, JsonHandler.py, imports.py
- Moduly vygenerované z Qt Creatoru, slouží pro generování .py modulů: LoadingScreen.ui, MainWindow.ui
- Moduly struktury aplikace vygenerované pomocí pyuic5: LoadingScreen.py, MainWindow.py
