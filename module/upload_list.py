import glob

def add_image(uri:str) -> str:
    dir = uri
    count_file = 0
    index = []
    files = glob.glob(dir+'*')
    # print(files)
    for file in files:
        count_file+=1
        index.append(file)
    
    # print(index[0])

    page_data = {}
    if count_file == 0:
        page_data['image'] = '画像は投稿されていません'
    else:
        page_data['image'] = '<li><img src = '+ index[0] +' width="350" height="200" alt="画像1"></li>'
        i=1
        for i in range(count_file):
            page_data['image'] = page_data['image'] + '<li><img src = '+ index[i] +' width="350" height="200" alt="画像'+str(i+1)+'"></li>'

    print(page_data)

    with open('./templates/upload_list.html','r') as f:
        html = f.read()
    f.closed

    for key, value in page_data.items():
        html = html.replace('{%' + key + '%}', value)
    return html