<!-- TOC -->

- [MySQL](#mysql)
    - [1.事务](#1事务)
    - [2.数据库索引](#2数据库索引)
    - [3.乐观锁和悲观锁](#3乐观锁和悲观锁)
    - [4.MVCC](#4MVCC)
    - [5.MyISAM和InnoDB](#5myisam%e5%92%8cinnodb)
    - [6.主键 超键 候选键 外键](#6主键-超键-候选键-外键)
    - [7.视图的作用，视图可以更改么？](#7视图的作用视图可以更改么)
    - [8.drop,delete与truncate的区别](#8dropdelete与truncate的区别)
    - [9.索引的工作原理及其种类](#9索引的工作原理及其种类)
    - [10.连接的种类](#10连接的种类)
    - [11.数据库优化的思路](#11数据库优化的思路)
    - [12.存储过程与触发器的区别](#12存储过程与触发器的区别)
    - [13.悲观锁和乐观锁是什么？](#13悲观锁和乐观锁是什么)
    - [14.你常用的mysql引擎有哪些?各引擎间有什么区别?](#13你常用的mysql引擎有哪些各引擎间有什么区别)

<!-- /TOC -->

## MySQL
### 1.事务

数据库事务(Database Transaction) ，是指作为单个逻辑工作单元执行的一系列操作，要么完全地执行，要么完全地不执行。
彻底理解数据库事务: http://www.hollischuang.com/archives/898

### 2.数据库索引

推荐: http://tech.meituan.com/mysql-index.html

[MySQL索引背后的数据结构及算法原理](http://blog.codinglabs.org/articles/theory-of-mysql-index.html)

聚集索引,非聚集索引,B-Tree,B+Tree,最左前缀原理

### 3.乐观锁和悲观锁

悲观锁：假定会发生并发冲突，屏蔽一切可能违反数据完整性的操作

乐观锁：假设不会发生并发冲突，只在提交操作时检查是否违反数据完整性。

乐观锁与悲观锁的具体区别: http://www.cnblogs.com/Bob-FD/p/3352216.html

### 4.MVCC

> ​	全称是Multi-Version Concurrent Control，即多版本并发控制，在MVCC协议下，每个读操作会看到一个一致性的snapshot，并且可以实现非阻塞的读。MVCC允许数据具有多个版本，这个版本可以是时间戳或者是全局递增的事务ID，在同一个时间点，不同的事务看到的数据是不同的。

### [MySQL](http://lib.csdn.net/base/mysql)的innodb引擎是如何实现MVCC的

innodb会为每一行添加两个字段，分别表示该行**创建的版本**和**删除的版本**，填入的是事务的版本号，这个版本号随着事务的创建不断递增。在repeated read的隔离级别（[事务的隔离级别请看这篇文章](http://blog.csdn.net/chosen0ne/article/details/10036775)）下，具体各种数据库操作的实现：

- select：满足以下两个条件innodb会返回该行数据：
  - 该行的创建版本号小于等于当前版本号，用于保证在select操作之前所有的操作已经执行落地。
  - 该行的删除版本号大于当前版本或者为空。删除版本号大于当前版本意味着有一个并发事务将该行删除了。
- insert：将新插入的行的创建版本号设置为当前系统的版本号。
- delete：将要删除的行的删除版本号设置为当前系统的版本号。
- update：不执行原地update，而是转换成insert + delete。将旧行的删除版本号设置为当前版本号，并将新行insert同时设置创建版本号为当前版本号。

其中，写操作（insert、delete和update）执行时，需要将系统版本号递增。

​由于旧数据并不真正的删除，所以必须对这些数据进行清理，innodb会开启一个后台线程执行清理工作，具体的规则是将删除版本号小于当前系统版本的行删除，这个过程叫做purge。

通过MVCC很好的实现了事务的隔离性，可以达到repeated read级别，要实现serializable还必须加锁。

> 参考：[MVCC浅析](http://blog.csdn.net/chosen0ne/article/details/18093187)

### 5.MyISAM和InnoDB

MyISAM 适合于一些需要大量查询的应用，但其对于有大量写操作并不是很好。甚至你只是需要update一个字段，整个表都会被锁起来，而别的进程，就算是读进程都无法操作直到读操作完成。另外，MyISAM 对于 SELECT COUNT(*) 这类的计算是超快无比的。

InnoDB 的趋势会是一个非常复杂的存储引擎，对于一些小的应用，它会比 MyISAM 还慢。他是它支持“行锁” ，于是在写操作比较多的时候，会更优秀。并且，他还支持更多的高级应用，比如：事务。

mysql 数据库引擎: http://www.cnblogs.com/0201zcr/p/5296843.html
MySQL存储引擎－－MyISAM与InnoDB区别: https://segmentfault.com/a/1190000008227211

### 6.主键 超键 候选键 外键

主键：数据库表中对存储数据对象予以唯一和完整标识的数据列或属性的组合。一个数据列只能有一个主键，且主键的取值不能缺失，即不能为空值(Null).

超键：在关系中能唯一标识元组的属性集称为关系模式的超键。一个属性可以作为一个超键，多个属性组合在一起也可以作为一个超键。超键包含候选键和主键。

候选键：是最小超键，即没有冗余元素的超键。

外键：在一个表中存在的另一个表的主键称此表的外键。

### 7.视图的作用，视图可以更改么？

视图是虚拟的表，与包含数据的表不一样，视图只包含使用时动态检索数据的查询;不包含任何列或数据。使用视图可以简化复杂的sql操作，隐藏具体的细节，保护数据;视图创建后，可以使用与表相同的方式利用它们。

视图不能被索引，也不能有关联的触发器或默认值，如果视图本身内有order by则对视图再次order by将被覆盖。

创建视图： create view xxx as xxxxxx

对于某些视图比如未使用联结子查询分组聚集函数Distinct Union等，是可以对其更新的，对视图的更新将对基表进行更新;但是视图主要用于简化检索，保护数据，并不用于更新，而且大部分视图都不可以更新。

### 8.drop,delete与truncate的区别

drop直接删掉表，truncate删除表中数据，再插入时自增长id又从1开始，delete删除表中数据，可以加where字句。

1.delete 语句执行删除的过程是每次从表中删除一行，并且同时将该行的删除操作作为事务记录在日志中保存以便进行回滚操作。truncate table则一次性地从表中删除所有的数据并不把单独的删除操作记录记入日志保存，删除行是不能恢复的。并且在删除的过程中不会激活与表有关的删除触发器，执行速度快。

2.表和索引所占空间。当表被truncate后，这个表和索引所占用的空间会恢复到初始大小，而delete操作不会减少表或索引所占用的空间。drop语句将表所占用的空间全释放掉。

3.一般而言，drop>truncate>delete

4.应用范围。truncate只能对table，delete可以是table和view

5.truncate和delete只删除数据，而drop则删除整个表（结构和数据)

6.truncate与不带where的delete:只删除数据，而不删除表的结构（定义）drop语句将删除表的结构被依赖的约束(constrain),触发器（trigger)索引(index);依赖于该表的存储过程/函数将被保留，但其状态会变为:invalid.

### 9.索引的工作原理及其种类

数据库索引，是数据库管理系统中一个排序的数据结构，以协助快速查询，更新数据库表中数据。索引的实现通常使用B树以其变种B+树。

在数据之外，数据库系统还维护着满足特定查找算法的数据结构，这些数据结构以某种方式引用（指向）数据，这样就可以在这些数据结构上实现高级查找算法。这种数据结构，就是索引。

为表设置索引要付出代价的：一是增加了数据库的存储空间，二是在插入和修改数据时要花费较多的时间（因为索引也要随之变动）

### 10.连接的种类
### 11.数据库优化的思路
### 12.存储过程与触发器的区别
### 13.悲观锁和乐观锁是什么？
### 14.你常用的mysql引擎有哪些?各引擎间有什么区别?
### 15.pg各个索引之间的区别和使用场景
开放的索引接口，使得PG支持非常丰富的索引方法，例如btree , hash , gin , gist , sp-gist , brin , bloom , rum , zombodb , bitmap (greenplum extend)，用户可以根据不同的数据类型，以及查询的场景，选择不同的索引。

PG内部还支持BitmapAnd, BitmapOr的优化方法，可以合并多个索引的扫描操作，从而提升多个索引数据访问的效率。

btree , hash , gin , gist , sp-gist , brin , bloom , rum , zombodb , bitmap
B-TREE索引通常支持的查询包括 > , < , = , <= , >= 以及排序。 目前大多数数据库都支持B-TREE索引方法。
hash索引通常支持
### 16.数据库sql的优化
- 索引的建立
- 减少group by字段，left join on 1=1多对一的情况使用min(xxx)
- 表结构的设计；构建临时表
- explain anylyse分析时间开销用在哪
- 求唯一值
  - `select distinct col from table ;  `
  - 
    ```
    with recursive skip as (    
      (    
        select min(t.sex) as sex from sex t where t.sex is not null    
      )    
      union all    
      (    
        select (select min(t.sex) as sex from sex t where t.sex > s.sex and t.sex is not null)     
          from skip s where s.sex is not null   
      )    
    )     
    select * from skip where sex is not null;   
    ```
- 递归收敛优化
  适用于，A表为主表，B表为记录表。 A表全扫，B表索引扫描了若干次（若干 = 唯一AID在B中出现的次数）。
  (quote)[https://github.com/digoal/blog/blob/master/201612/20161201_01.md];
  (quote)[https://github.com/digoal/blog/blob/master/201705/20170519_01.md?spm=a2c6h.12873639.0.0.45131bffXcMf5X&file=20170519_01.md]
  - 建表
    
  create table a(id int primary key, info text);

  create table b(id int primary key, aid int, crt_time timestamp);
  create index b_aid on b(aid);
  - 插入测试数据
  -- a表插入1000条
  insert into a select generate_series(1,1000), md5(random()::text);

  -- b表插入500万条，只包含aid的500个id。
  insert into b select generate_series(1,5000000), generate_series(1,500), clock_timestamp();
  - 原始sql`select * from a where id not in (select aid from b); `
  - 优化1`select a.id from a left join b on (a.id=b.aid) where b.* is null;`
  - 递归收敛优化
  ```
  select * from a where id not in 
    (
  with recursive skip as (  
    (  
      select min(aid) aid from b where aid is not null  
    )  
    union all  
    (  
      select (select min(aid) aid from b where b.aid > s.aid and b.aid is not null)   
        from skip s where s.aid is not null  
    )  -- 这里的where s.aid is not null 一定要加,否则就死循环了.  
  )   
  select aid from skip where aid is not null
  );
  ```

- sub_query优化
  适用于 A表全扫，B表索引扫描了若干次（若干 = A表记录数）。
  (quote)[https://yq.aliyun.com/roundtable/56354]
  场景表述
  一张小表A，里面存储了一些ID，大约几百个。
  （比如说巡逻车辆ID，环卫车辆的ID，公交车，微公交的ID）。
  另外有一张日志表B，每条记录中的ID是来自前面那张小表的，但不是每个ID都出现在这张日志表中，比如说一天可能只有几十个ID会出现在这个日志表的当天的数据中。 
  （比如车辆的行车轨迹数据，每秒上报轨迹，数据量就非常庞大）。 
  那么我怎么快速的找出今天没有出现的ID呢。
  （哪些巡逻车辆没有出现在这个片区，是不是偷懒了？哪些环卫车辆没有出行，哪些公交或微公交没有出行）？
  ```
postgres=# explain (analyze,timing) select * from a where id not in (select aid from b); 
                                                       QUERY PLAN                                                       
------------------------------------------------------------------------------------------------------------------------
 Seq Scan on a  (cost=179053.25..179074.76 rows=500 width=37) (actual time=4369.478..4369.525 rows=100 loops=1)
   Filter: (NOT (hashed SubPlan 1))
   Rows Removed by Filter: 901
   SubPlan 1
     ->  Seq Scan on b  (cost=0.00..154053.60 rows=9999860 width=4) (actual time=0.322..1829.342 rows=10000000 loops=1)
 Planning time: 0.094 ms
 Execution time: 4423.364 ms
(7 rows)

postgres=# explain (analyze,timing) select a.* from a left join b on (a.id=b.aid) where b.* is null;
                                                      QUERY PLAN                                                       
-----------------------------------------------------------------------------------------------------------------------
 Hash Right Join  (cost=31.52..280244.69 rows=49999 width=37) (actual time=4316.767..4316.790 rows=100 loops=1)
   Hash Cond: (b.aid = a.id)
   Filter: (b.* IS NULL)
   Rows Removed by Filter: 10000000
   ->  Seq Scan on b  (cost=0.00..154053.60 rows=9999860 width=44) (actual time=0.013..2544.321 rows=10000000 loops=1)
   ->  Hash  (cost=19.01..19.01 rows=1001 width=37) (actual time=0.342..0.342 rows=1001 loops=1)
         Buckets: 1024  Batches: 1  Memory Usage: 76kB
         ->  Seq Scan on a  (cost=0.00..19.01 rows=1001 width=37) (actual time=0.009..0.137 rows=1001 loops=1)
 Planning time: 0.173 ms
 Execution time: 4316.828 ms
(10 rows)
  ```
  - sql优化
  ```
  select * from a 
  where (select aid from b where b.aid=a.id limit 1) is null;  -- sub query is NULL, 是不是很给力呢
  ```