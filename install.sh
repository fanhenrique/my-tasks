zip -r ./app.zip *
echo '#!/usr/bin/python3' | cat - app.zip > mytasks
rm app.zip
chmod +x mytasks
sudo mv mytasks /usr/bin/