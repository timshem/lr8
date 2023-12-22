def IncTime(H, M, S, T):
    total_seconds = H * 3600 + M * 60 + S  
    total_seconds += T  
    H = total_seconds // 3600  
    total_seconds %= 3600
    M = total_seconds // 60  
    S = total_seconds % 60  
    return H, M, S


H = int(input())  
M = int(input())  
S = int(input())  
T = int(input())
if H > 0 and M > 0 and S > 0 and T > 0:
    new_H, new_M, new_S = IncTime(H, M, S, T)
    print(f"Новое время: {new_H} часов, {new_M} минут, {new_S} секунд")
else:
    print('error')