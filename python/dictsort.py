d={'AJ':21,'Abhi':20,'mruthul':22}
print("acending order")
print(sorted(d.items(),key=lambda x:x[1]))
print("Decending order")
print(sorted(d.items(),key=lambda x:x[1],reverse=1))


