import whois

domain = " "  # whois sorgusu yapmak istenilen domain

result = whois.whois(domain) #sorgu yapılır
print("Domain Adı:", result.domain_name) #domain_name bilgisi yazdırılır
print(result) #whois ile sorgulanabilen tüm bilgiler yazdırılır
