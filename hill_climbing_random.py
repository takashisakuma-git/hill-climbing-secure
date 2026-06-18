import sys
from csclib import *
import random
import time

def hill_climbing(max_iterations: int, initial_solution: Share, weights: list, capacity: Share, agent_A: Share, agent_B: Share, patience:int) -> Share:
    current_solution = initial_solution
    print("\ncurrent_solution")
    current_solution.print()

    cse = current_solution.extend(2)
    print("cse:")
    cse.print()

    VA_current = calculate_VA(cse, agent_A)
    VB_current = calculate_VB(cse, agent_B)
    V_current = VA_current + VB_current
    
    iteration = 0
    no_improvement_count = 0
    cnt = 0
        
    while iteration < max_iterations and no_improvement_count < patience:
        new_solution = generate_new_solution(cse)

        while not is_valid_solution(new_solution, weights, capacity):
            print("重みチェックオーバー")
            new_solution = generate_new_solution(cse)

        VA_new = calculate_VA(new_solution, agent_A)
        VB_new = calculate_VB(new_solution, agent_B)
        V_new = VA_new + VB_new
    
        if V_new > V_current:
            cse = new_solution
            V_current = V_new
            nice_solution = cse
            print("⭐︎nice_solution発見⭐︎")
            no_improvement_count = 0
        else:
            no_improvement_count += 1
            
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
    total = 0
    agent_solution = solution.extend(1024)
    for i in range(len(solution)):
        total += agent_A[i] * agent_solution[i]
    return total

def calculate_VB(solution: Share, agent_B: Share) -> Share:
    total = 0
    agent_solution = solution.extend(1024)
    for i in range(len(solution)):
        total += agent_B[i] * agent_solution[i]
    return total

def generate_new_solution(cse: Share) -> Share:
    new_solution = cse.dup()
    
    index_to_change = random_index(new_solution)
    print("\nindex_to_change ["f"{index_to_change}" "]")
    new_solution[index_to_change] += 1
    new_solution.print()
    return new_solution

def is_valid_solution(solution: Share, weights: list, capacity: Share) -> bool:
    total_weight = 0
    hoge_solution = solution.extend(1024)
    for i in range(len(solution)):
        total_weight += weights[i] * hoge_solution[i]
    return total_weight <= capacity

def random_index(solution: Share):
    return random.randint(0, len(solution) - 1)

def main():
    random.seed(0) # for debug
    start_time = time.time()
    
    q = 2**10

    initial_solution = Share([0, 0, 0, 0, 0, 0], q)
    print("initial_solution")
    initial_solution.print()
  
    agent_A = Share([12, 13, 8, 10, 25, 18], q)
    print("agent_A:")
    agent_A.print()
  
    agent_B = Share([18, 25, 10, 8, 13, 12], q)
    print("agent_B:")
    agent_B.print()
  
    capacity = Share([65],q)
    print("capacity")
    capacity.print()

    weights = [10, 12, 7, 9, 21, 16]
    max_iterations = 100
    patience = 20
  
    final_solution, final_value = hill_climbing(max_iterations, initial_solution, weights, capacity, agent_A, agent_B, patience)
    print("\nFinal_solution:")
    final_solution.print()
    print(f"Total benefit of the final solution:")
    final_value.print()
    
    print(f"this party number is {party}")

    end_time = time.time()
    elapsed_time = end_time - start_time
    
    print(f"開始時刻: {start_time:.6f} 秒")
    print(f"終了時刻: {end_time:.6f} 秒")    
    print(f"処理時間: {elapsed_time:.6f} 秒")
    
if __name__ == '__main__':
  party = -1

  args = sys.argv
  if len(args) >= 2:
    party = int(args[1])
  Csclib_start(party)

  main()
