# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import matplotlib.pyplot as plt
import pickle

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    fig, (ax1, ax2) = plt.subplots(1, 2)
    ax1.set_xlabel("Iterations")
    ax1.set_ylabel("Reward")
    ax1.set_title("Mean 100-Episode Rewards")
    ax2.set_xlabel("Iterations")
    ax2.set_ylabel("Reward")
    ax2.set_title("Best Mean Rewards")
    with open('learning_freq\\best_params.pkl', 'rb') as f:
        data = pickle.load(f)
        Y1 = data['mean_episode_rewards']
        Y2 = data['best_mean_episode_rewards']
        X = [i for i in range(len(Y1))]
        ax1.plot(X, Y1, "b", label="LF=1", )
        ax2.plot(X, Y2, "b", )
    with open('learning_freq\lf4.pkl', 'rb') as f:
        data = pickle.load(f)
        Y1 = data['mean_episode_rewards']
        Y2 = data['best_mean_episode_rewards']
        X = [i for i in range(len(Y1))]
        ax1.plot(X, Y1, "r", label="LF=4", )
        ax2.plot(X, Y2, "r")
    with open('learning_freq\lf7.pkl', 'rb') as f:
        data = pickle.load(f)
        Y1 = data['mean_episode_rewards']
        Y2 = data['best_mean_episode_rewards']
        X = [i for i in range(len(Y1))]
        ax1.plot(X, Y1, "y", label="LF=7", )
        ax2.plot(X, Y2, "y")
    with open('learning_freq\lf10.pkl', 'rb') as f:
        data = pickle.load(f)
        Y1 = data['mean_episode_rewards']
        Y2 = data['best_mean_episode_rewards']
        X = [i for i in range(len(Y1))]
        ax1.plot(X, Y1, "g", label="LF=10", )
        ax2.plot(X, Y2, "g")
    
    fig.suptitle("Learning Frequency Analysis", fontsize=20)
    fig.legend(loc="upper left")
    # fig.show()

    fig, (ax1, ax2) = plt.subplots(1, 2)
    ax1.set_xlabel("Iterations")
    ax1.set_ylabel("Reward")
    ax1.set_title("Mean 100-Episode Rewards")
    ax2.set_xlabel("Iterations")
    ax2.set_ylabel("Reward")
    ax2.set_title("Best Mean Rewards")
    with open('learning_freq\\best_params.pkl', 'rb') as f:
        data = pickle.load(f)
        Y1 = data['mean_episode_rewards']
        Y2 = data['best_mean_episode_rewards']
        ymin = min(min(len(Y1), len(Y2)), 2000000)
        X = [i for i in range(ymin)]
        ax1.plot(X, Y1[:2000000], "b", label="LR=0.00025", )
        ax2.plot(X, Y2[:2000000], "b", )
    with open('learning_rate\lr05.pkl', 'rb') as f:
        data = pickle.load(f)
        Y1 = data['mean_episode_rewards']
        Y2 = data['best_mean_episode_rewards']
        ymin = min(min(len(Y1), len(Y2)), 2000000)
        X = [i for i in range(ymin)]
        ax1.plot(X, Y1[:2000000], "r", label="LR=0.5", )
        ax2.plot(X, Y2[:2000000], "r")
    with open('learning_rate\lr0001.pkl', 'rb') as f:
        data = pickle.load(f)
        Y1 = data['mean_episode_rewards']
        Y2 = data['best_mean_episode_rewards']
        ymin = min(min(len(Y1), len(Y2)), 2000000)
        X = [i for i in range(ymin)]

        ax1.plot(X, Y1[:2000000], "y", label="LR=0.001", )
        ax2.plot(X, Y2[:2000000], "y")
    with open('learning_rate\lr00001.pkl', 'rb') as f:
        data = pickle.load(f)
        Y1 = data['mean_episode_rewards']
        Y2 = data['best_mean_episode_rewards']
        ymin = min(min(len(Y1), len(Y2)), 2000000)
        X = [i for i in range(ymin)]
        ax1.plot(X, Y1[:2000000], "g", label="LR=0.0001", )
        ax2.plot(X, Y2[:2000000], "g")
    
    fig.suptitle("Learning Rate Analysis", fontsize=20)
    fig.legend(loc="upper left")
    # fig.show()

    '''
    plt.title("Q1")
    with open('learning_freq\\best_params.pkl', 'rb') as f:
        data = pickle.load(f)
        Y1 = data['mean_episode_rewards']
        Y2 = data['best_mean_episode_rewards']
        X = [i for i in range(len(Y1))]
        plt.plot(X, Y1, "r", label='Mean 100-episode rewards')
        plt.plot(X, Y2, "g", label='best mean episode rewards')
        plt.text(0,0,'learning_freq=1\noptimizer=Adam\ntarget_update_freq=1000\nreplay_buffer_size=100000', fontsize=8)
    plt.xlabel("Iteration")
    plt.ylabel("Reward")
    plt.legend(loc="upper left")
    #plt.show()

'''

