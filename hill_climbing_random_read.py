import sys
from csclib import *
# import random
import glob
import time

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

    # ファイルを探してリストを取得
    file_list = glob.glob("random_index_*.txt")
    if not file_list:  # ファイルが見つからない場合
        print("No random index files found.")
        return  # 処理を終了
    
    # 最新のファイルを取得
    latest_file = max(file_list, key=lambda x: x)
    # ファイル名を確認
    print(f"\nUsing latest file: {latest_file}")
    
    # 不必要ではないのか
    # ファイルから乱数を読み込む
    # random_numbers = read_all_random_numbers(latest_file)
    # print(f"Random numbers: {random_numbers}")
    
    # 乱数ジェネレータを作成
    index_gen = random_index(latest_file)
        
    while iteration < max_iterations and no_improvement_count < patience:
        # Mediatorが有効な解の更新案を作成
        file_path = latest_file
        new_solution = generate_new_solution(cse, index_gen)

        # 重みチェックに通るまで更新案を生成し続ける
        while not is_valid_solution(new_solution, weights, capacity):
            print("重みチェックオーバー")
            new_solution = generate_new_solution(cse, index_gen)

        # Agent_AとAgnet_Bが新しい解の利得を計算
        VA_new = calculate_VA(new_solution, agent_A)
        VB_new = calculate_VB(new_solution, agent_B)
        V_new = VA_new + VB_new

        # 暫定解を比較し、大きい方を次の解候補に設定
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

def read_all_random_numbers(file_path: str) -> list[int]:
    """ファイルから全ての乱数をリストとして読み込む"""
    numbers = []
    try:
        with open(file_path, "r") as file:
            for line in file:
                line = line.strip()
                if line.isdigit():
                    numbers.append(int(line))
                else:
                    print(f"Skipping invalid line: {line}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except ValueError as e:
        print(f"Error reading file: {e}")
    return numbers

def random_index(file_path: str):
    """ファイルから乱数を順番に取り出すジェネレータ"""
    random_numbers = read_all_random_numbers(file_path)
    print(f"\nRandom numbers: {random_numbers}")
    for index in random_numbers:
        yield index  # 乱数を1つずつ返す

def generate_new_solution(cse: Share, index_gen) -> Share:
    """次の乱数を利用してソリューションを更新"""
    new_solution = cse.dup()
    
    try:
        # ジェネレータから次の乱数を取得
        index_to_change = next(index_gen)
        print("\nindex_to_change ["f"{index_to_change}" "]")
        if 0 <= index_to_change < len(new_solution):  # 範囲内かを確認
            new_solution[index_to_change] += 1
            # print(f"Updated new_solution:")
            new_solution.print()
        else:
            print(f"Index {index_to_change} is out of range for the array.")
    except StopIteration:
        print("No more random numbers to process.")
    
    return new_solution

def is_valid_solution(solution: Share, weights: list, capacity: Share) -> bool:
    # 解の重みが容量内に収まっているかをチェックするロジック
    total_weight = 0
    hoge_solution = solution.extend(1024)
    for i in range(len(solution)):
        total_weight += weights[i] * hoge_solution[i]
    return total_weight <= capacity

#def random_index(solution: Share):
#    # リストのランダムなインデックスを返す
#    return random.randint(0, len(solution) - 1)

def main():
    start_time = time.time()  # 開始時間を記録
    
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

    end_time = time.time()  # 終了時間を記録
    elapsed_time = end_time - start_time
    
    print(f"this party number is {party}")
    
    print(f"開始時刻: {start_time:.6f} 秒")  # 開始時刻を表示
    print(f"終了時刻: {end_time:.6f} 秒")  # 終了時刻を表示
    print(f"処理時間: {elapsed_time:.6f} 秒")
    
if __name__ == '__main__':
  party = -1

  args = sys.argv
  if len(args) >= 2:
    party = int(args[1])
  Csclib_start(party)

  main()
