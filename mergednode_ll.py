#COuldnt get it on my own. The trick was amazing.
#https://www.hackerrank.com/challenges/find-the-merge-point-of-two-joined-linked-lists/problem
def findMergeNode(head1, head2):
    nodea=head1
    nodeb=head2
    while nodea!=nodeb:
        if nodea is None:
            nodea=head2
        else:
            nodea=nodea.next
        if nodeb is None:
            nodeb=head1
        else:
            nodeb=nodeb.next
    return nodea.data