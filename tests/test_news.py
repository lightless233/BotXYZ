import requests
from bs4 import BeautifulSoup

target_url = "https://sec.today/pulses/"

response = requests.get(target_url)
# print(response.text)

soup = BeautifulSoup(response.text)

"""
<div class="card my-2">
 <div class="card-body">
  <h5 class="card-title">
   <a class="text-dark" href="/pulses/ae7176c4-42ee-4886-bb63-4f24df15ab1c/" rel="noopener" target="_blank">
    Persistence – Winlogon Helper DLL
   </a>
  </h5>
  <small class="card-subtitle text-muted">
   pentestlab.blog
•
   <span class="badge badge-tag">
    Pentest
   </span>
  </small>
  <p class="card-text my-1">
   <q>
    以红队角度来对Windows的Winlogo（用户登录程序）安全讨论。
   </q>
   –
   <cite>
    <a class="text-muted" href="/user/8eb60fcc-f278-42e6-a76f-46a845ee9865/pushes/">
     lanying37
    </a>
    <span class="text-muted">
     <small>
      • 8 hours ago
     </small>
    </span>
   </cite>
  </p>
  <p class="card-text mr-3">
   <i class="star-button far fa-star fa-xs text-muted" onclick="star_card(this, 36, 'ae7176c4-42ee-4886-bb63-4f24df15ab1c')">
   </i>
   <small class="star-count d-inline-block text-muted">
    0
   </small>
  </p>
 </div>
</div>
"""
articles = soup.find_all("div", "my-2")
# print(articles[0].prettify())
x = articles[0].find_all("a")
print(x[0])

print(x[0]['href'])
print(x[0].text)
