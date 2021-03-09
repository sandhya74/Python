#dict={"praveen":8734567289,"abi":978634563,45:"anitha"}
#print(dict["praveen"])
#print(dict.get("abi"))
#dict.update({"praveen": 960083768})
#dict.update({45:"sandhya"})
#print(dict)
#print(dict.keys())
#print(dict.values())
#print(dict.items())

#print(dict.pop({"praveen": 960083768}))
#std={12:"gowri"}
#staff={13:"kavya",12:"gopi"}
#std.Fromkeys(staff)

sub={"math","cs","science"}
mark={120,150,130}
sub_mark=dict(zip(sub,mark))
print(sub_mark)
total={key:value/2 for key,value in zip(sub,mark)}
print(total)

