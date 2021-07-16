clear;close all
m_data=.5;
c_data=1;
noise=0.3;
% x=[0.5:0.1:3.5];
% y_data=m_data.*x+c_data+noise*randn(size(x));
x=[2,3,7];
y_data=[1,5,9];
y_fit=m_data.*x+c_data;
r_fit=y_fit-y_data;
S_fit=sum(r_fit.^2);
x_lim=[0,8];

m_0=sum((x-mean(x)).*y_data)/sum((x-mean(x)).^2);
c_0=mean(y_data)-m_0*mean(x);

m_1=0.3;
c_1=1.5;
m_2=-2;
c_2=3;
m_3=2;
c_3=-1.5;

S_fun = @(m,c) sum((y_data-(m*x+c)).^2);

%% Plotting
Fig=figure(...
    'Units','normalized',...
    'Position',[.33 .5 .63 .4],...
    'Color',[1 1 1],...%    'renderer','painters',...
    'WindowStyle','normal',...
    'PaperPositionMode','auto',...
    'PaperOrientation','landscape');
subplot(1,2,1);
hold on
h=plot(x,y_data,'x','markersize',8,'linewidth',2,'color',[0,0,0]);
for i=1:length(x)
    plot([x(i) x(i)], [y_data(i) m_0*x(i)+c_0],'k')
    % plot([x(i) x(i)], [y_data(i) m_1*x(i)+c_1],'r')
end
plot(x_lim,m_0*x_lim+c_0,'k:','linewidth',2);
plot(x_lim,m_1*x_lim+c_1,'r:','linewidth',2);
plot(x_lim,m_2*x_lim+c_2,'g:','linewidth',2);
plot(x_lim,m_3*x_lim+c_3,'b:','linewidth',2);
xlim(x_lim)
ylim([0,10])
hold off
set(gca,'TickLabelInterpreter','latex',...
    'LineWidth',1.2,...
    'FontSize',16);
xlabel('$x$','Interpreter','latex');
ylabel('$y$','Interpreter','latex');
axis square
box
leg=legend('Data','Residuals', 'location','northwest')
set(leg,'interpreter','latex')

subplot(1,2,2);
ms=-4:0.1:4;
cs=-4:0.1:4;
[M,C]=meshgrid(ms,cs);
axis square
for i=1:length(ms)
    for j=1:length(cs)
        S(i,j)=S_fun(M(i,j),C(i,j));
    end
end
contourf(M,C,log(S),10)
colormap(flipud(pink));%flipud
xlabel('$m$','Interpreter','latex');
ylabel('$c$','Interpreter','latex');
set(gca,'TickLabelInterpreter','latex',...
    'LineWidth',1.2,...
    'FontSize',16)
hold on
plot(m_0,c_0,'*','markersize',12,'linewidth',2,'color',[0,0,0]);
plot(m_1,c_1,'*','markersize',12,'linewidth',2,'color',[1,0,0]);
plot(m_2,c_2,'*','markersize',12,'linewidth',2,'color',[0,1,0]);
plot(m_3,c_3,'*','markersize',12,'linewidth',2,'color',[0,0,1]);
hold off

colo=colorbar;
set(colo,'FontSize',16, 'TickLabelInterpreter','latex')
ylabel(colo,'log($S$)','Interpreter','latex')