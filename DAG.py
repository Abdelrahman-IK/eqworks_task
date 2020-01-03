
class DAG:

    def __init__(self):
        """
        Init function loads relation.txt as relations between tasks.
        loads tasks_ids.txt as each task's id.
        loads question.txt as the start task and goal task.
        """
        try:
            self.relations = open("DAG_data/relations.txt", "r").read().replace('->', ',')
            self.relations = [tuple(i.split(',')) for i in self.relations.split('\n')]
            self.ids = list(open("DAG_data/task_ids.txt", "r").read().split(','))
            self.question = [int(s) for s in open("DAG_data/question.txt", "r").read().split() if s.isdigit()]
            self.start = str(self.question[0])
            self.target = str(self.question[-1])
            self.path = [self.target]
        except Exception as ex:
            print(str(ex))

    def sorting(self):
        """
        Sorting function finds the correct topological ordering of the DAG
        based on the start task and goal task.
        :return: List of ordered tasks
        """
        try:
            for i in self.path:
                for x in self.relations:
                    if x[1] == i and x[0] not in self.path:
                        self.path.append(x[0])
                if i == self.start:
                    break
            return self.path[::-1]
        except Exception as ex:
            print(str(ex))


if __name__ == '__main__':
    dag = DAG()
    print(dag.sorting())
