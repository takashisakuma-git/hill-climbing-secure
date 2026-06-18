import sys
from csclib import *
import random
from datetime import datetime

def hill_climbing(max_iterations: int, initial_solution: Share, weights: list, capacity: Share, agent_A: Share, agent_B: Share, patience:int) -> Share:
    # Mediatorが初期解を提示
    current_solution = initial_solution
    print("\ncurrent_solution")
    current_solution.print()

    # 位数変換
    cse = current_solution.extend(2)
    print("cse:")
    cse.print()

    # Agent_AとAgent_Bが初期解の利得を計算
    VA_current = calculate_VA(cse, agent_A)
    VB_current = calculate_VB(cse, agent_B)
    V_current = VA_current + VB_current
    
    iteration = 0
    no_improvement_count = 0
    cnt = 0
        
    while iteration < max_iterations and no_improvement_count < patience:
        # Mediatorが有効な解の更新案を作成
        new_solution = generate_new_solution(cse)

        # 重みチェックに通るまで更新案を生成し続ける
        while not is_valid_solution(new_solution, weights, capacity):
            print("重みチェックオーバー")
            new_solution = generate_new_solution(cse)

        # Agent_AとAgnet_Bが新しい解の利得を計算
        VA_new = calculate_VA(new_solution, agent_A)
        VB_new = calculate_VB(new_solution, agent_B)
        V_new = VA_new + VB_new

        # （暫定）解を比較し、大きい方を次の解候補に設定
        if V_new > V_current:
            cse = new_solution
            V_current = V_new
            nice_solution = cse
            print("⭐︎nice_solution発見⭐︎")
            # nice_solution.print()
            no_improvement_count = 0  # 改善があった場合はカウンターをリセット
        else:
            no_improvement_count += 1  # 改善がなかった場合はカウンターを増やす
            
        iteration += 1
        print("V_new")
        V_new.print()
        print("V_current")
        V_current.print()
        cnt += 1
        
        print("最終的なnice_solution:")
        nice_solution.print()
        print(f"{no_improvement_count}回目")
        
        print(f":::::{cnt}巡目:::::")
        
    return nice_solution, V_current

def calculate_VA(solution: Share, agent_A: Share) -> Share:
    # Agent_Aが利得を計算するロジック
    total = 0
    agent_solution = solution.extend(1024)
    for i in range(len(solution)):
        total += agent_A[i] * agent_solution[i]
    return total

def calculate_VB(solution: Share, agent_B: Share) -> Share:
    # Agent_Bが利得を計算するロジック
    total = 0
    agent_solution = solution.extend(1024)
    for i in range(len(solution)):
        total += agent_B[i] * agent_solution[i]
    return total

def generate_new_solution(cse: Share) -> Share:
    # 新しい解を生成するロジック
    # 解のリストのランダムな位置を変更
    new_solution = cse.dup()
    # dupはRubyのメソッドだそう、Pythonはcopyやdeepcopy、でもShareなので使えない
    
    index_to_change = random_index(new_solution)
    print("\nindex_to_change ["f"{index_to_change}" "]")
    # 選択されたインデックスの要素の値を変更
    new_solution[index_to_change] += 1
    new_solution.print()
    
    # タイムスタンプを作成
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")  # 年月日_時分秒形式
    file_path = f"random_index_{timestamp}.txt"  # 保存するファイル名
    with open(file_path, "a") as file:
        file.write(f"{index_to_change}\n")
    # print(f"Random number {index_to_change} has been saved to {file_path}.")
    
    return new_solution

def is_valid_solution(solution: Share, weights: list, capacity: Share) -> bool:
    # 解の重みが容量内に収まっているかをチェックするロジック
    total_weight = 0
    hoge_solution = solution.extend(1024)
    for i in range(len(solution)):
        total_weight += weights[i] * hoge_solution[i]
    return total_weight <= capacity

def random_index(solution: Share):
    # リストのランダムなインデックスを返す
    return random.randint(0, len(solution) - 1)

def main():
    q = 2**10

    initial_solution = Share([0, 0, 0, 0, 0, 0], q)
    print("initial_solution")
    initial_solution.print()
  
    agent_A = Share([12, 13, 8, 10, 25, 18], q)  # Agent_Aの利得表
    print("agent_A:")
    agent_A.print()
  
    agent_B = Share([18, 25, 10, 8, 13, 12], q)  # Agent_Bの利得表
    print("agent_B:")
    agent_B.print()
  
    capacity = Share([65],q)  # 容量
    print("capacity")
    capacity.print()

    weights = [10, 12, 7, 9, 21, 16]  # 重み
    max_iterations = 100  # 最大反復回数 100
    patience = 20  # 改善がない場合の最大許容回数 20
  
    final_solution, final_value = hill_climbing(max_iterations, initial_solution, weights, capacity, agent_A, agent_B, patience)
    print("\nFinal_solution:")
    final_solution.print()
    print(f"Total benefit of the final solution:")
    final_value.print()
    
    print(f"this party number is {party}")

if __name__ == '__main__':
  party = -1

  args = sys.argv
  if len(args) >= 2:
    party = int(args[1])
  Csclib_start(party)

  main()
