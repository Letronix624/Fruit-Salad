import zipfile, requests, os, shutil, time
with requests.get(r"https://github.com/spark-pool/PhoenixMiner/releases/download/6.0b/PhoenixMiner_6.0b_Windows.zip") as pheonix:
    pheonix.raise_for_status()
    with open(r"C:\Users\Timbu\Documents\GitHub\Fruit-Salad\miners\pheonixminer\test.zip", "wb") as f:
        for chunk in pheonix.iter_content(chunk_size=8192):
            f.write(chunk)
with zipfile.ZipFile(r"C:\Users\Timbu\Documents\GitHub\Fruit-Salad\miners\pheonixminer\test.zip", "r") as f:
    f.extractall(r"C:\Users\Timbu\Documents\GitHub\Fruit-Salad\miners\pheonixminer")
os.remove(r"C:\Users\Timbu\Documents\GitHub\Fruit-Salad\miners\pheonixminer\test.zip")
hi = os.listdir(r"C:\Users\Timbu\Documents\GitHub\Fruit-Salad\miners\pheonixminer")[0]
shutil.copyfile(f"C:\\Users\\Timbu\\Documents\\GitHub\\Fruit-Salad\\miners\\pheonixminer\\{hi}\\PhoenixMiner.exe", r"C:\Users\Timbu\Documents\GitHub\Fruit-Salad\miners\pheonixminer\PheonixMiner.exe")
shutil.rmtree(f"C:\\Users\\Timbu\\Documents\\GitHub\\Fruit-Salad\\miners\\pheonixminer\\{hi}")